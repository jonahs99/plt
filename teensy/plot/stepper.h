#include <Arduino.h>

// To use, include this header file, and call initStepperPins at setup
// Then you can call startSteppers whenever steppersStopped is true

const int N_MOTORS = 2;
const int dirPins[] = { 13, 15 };
const int stepPins[] = { 14, 16 };

IntervalTimer timer0;
IntervalTimer timer1;
IntervalTimer timers[] = { timer0, timer1 };
volatile int stepsLeft[] = { 0, 0 };
volatile bool steppersStopped = true;

void stepMotor(int motorIdx) {
    if (stepsLeft[motorIdx] > 0) {
        stepsLeft[motorIdx]--;
        digitalWrite(stepPins[motorIdx], HIGH);
        delayMicroseconds(3);
        digitalWrite(stepPins[motorIdx], LOW);
    } else {
        steppersStopped = true;
        for (int i = 0; i < N_MOTORS; i++) {
            if (stepsLeft[i] > 0) steppersStopped = false;
        }
    }
}

void stepMotor0() {
    stepMotor(0);
}

void stepMotor1() {
    stepMotor(1);
}

void (* stepMotorFns[]) = { stepMotor0, stepMotor1 };

void initStepperPins() {
    for (int i = 0; i < N_MOTORS; i++) {
        pinMode(dirPins[i], OUTPUT);
        pinMode(stepPins[i], OUTPUT);
    }
}

void startSteppers(int steps[], int intervals[]) {
    noInterrupts();
    for (int i = 0; i < N_MOTORS; i++) {
        stepsLeft[i] = abs(steps[i]);
        digitalWrite(dirPins[i], steps[i] > 0 ? HIGH : LOW);
    }
    steppersStopped = false;
    for (int i = 0; i < N_MOTORS; i++) {
        timers[i].begin(stepMotorFns[i], intervals[i]);
    }
    interrupts();
}
