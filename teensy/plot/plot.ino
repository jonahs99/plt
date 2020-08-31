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
    if (steppersReady()) {
        if (commandsInBuffer > 0) {
            // Pop a command from the buffer
            Command cmd = commandBuffer[commandBack];
            commandBack = (commandBack + 1) % BUFFER_LEN;
            commandsInBuffer -= 1;
            doCommand(cmd);
        }
    }
    
    readInput();
}

long stepPosition[N_MOTORS] = { 0, 0 };

void doCommand(Command cmd) {
    // Convert mm to step target
    const long steps_per_mm = 80;
    long stepTarget[N_MOTORS];
    for (int i = 0; i < N_MOTORS; i++) {
        stepTarget[i] = cmd.pos[i] * steps_per_mm;
    }
    long stepsToMove[N_MOTORS];
    for (int i = 0; i < N_MOTORS; i++) {
        stepsToMove[i] = stepTarget[i] - stepPosition[i];
    }

    // Compute step speed
    long dist = 0;
    for (int i = 0; i < N_MOTORS; i++) {
      dist += stepsToMove[i] * stepsToMove[i];
    }
    dist = sqrt(dist);
    if (dist == 0) return;
    long totalTime = dist * ((double) 60 * (double) 1000000 / (double) steps_per_mm / (double) cmd.feed);

    // Update to the new position
    memcpy(stepPosition, stepTarget, sizeof(stepPosition));

    // Start moving!
    startSteppers(stepsToMove, totalTime);
}
