#include "stepper.h"
#include "gcode.h"

const int ledPin = 13;

void setup() {
    pinMode(ledPin, OUTPUT);
    initStepperPins();

    Serial.begin(250000);
    Serial.setTimeout(10000);

    Serial.println("ok");
}

void loop() {
    noInterrupts();
    bool stopped = steppersStopped;
    interrupts();

    if (stopped) {
        if (commandsInBuffer > 0) {
            // Pop a command from the buffer
            Command cmd = commandBuffer[commandBack];
            commandBack = (commandBack + 1) % BUFFER_LEN;
            commandsInBuffer -= 1;
            doCommand(cmd);
        }
    }
    
    if (commandsInBuffer < BUFFER_LEN / 2) {
        while (readInput()) { }
    }
}

int stepPosition[N_MOTORS] = { 0, 0 };

void doCommand(Command cmd) {
    // Convert mm to step target
    const int steps_per_mm = 80;
    int stepTarget[N_MOTORS];
    for (int i = 0; i < N_MOTORS; i++) {
        stepTarget[i] = cmd.pos[i] * steps_per_mm;
    }
    int stepsToMove[N_MOTORS];
    for (int i = 0; i < N_MOTORS; i++) {
        stepsToMove[i] = stepTarget[i] - stepPosition[i];
    }

    // Compute step speed
    long dist = 0;
    for (int i = 0; i < N_MOTORS; i++) {
      dist += sq(stepsToMove[i]);
    }
    dist = sqrt(dist);
    if (dist == 0) return;

    long totalTime = dist * 60 * 1000000 / steps_per_mm / cmd.feed;
    int intervals[N_MOTORS];
    for (int i = 0; i < N_MOTORS; i++) {
        intervals[i] = totalTime / abs(stepsToMove[i]);
    }

    // Update to the new position
    memcpy(stepPosition, stepTarget, sizeof(stepPosition));

    // Start moving!
    startSteppers(stepsToMove, intervals);
}
