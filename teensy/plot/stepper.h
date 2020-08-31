#include <Arduino.h>

// To use, include this header file, and call initStepperPins at setup
// Then you can call startSteppers whenever steppersReady() is true

const int N_MOTORS = 2;
const int dirPins[] = { 13, 15 };
const int stepPins[] = { 14, 16 };

IntervalTimer _stepperTimer;
const int _stepperTimerInterval = 4;

volatile long _stepCount = 0;
volatile long _stepTargets[] = { 0, 0 };
volatile long _stepCurrent[] = { 0, 0 };
volatile long _stepD[] = { 0, 0 }; // For bresenham's line algorithm

void _stepMotors() {
    for (int i = 0; i < N_MOTORS; i++) {
        if (_stepCurrent[i] >= _stepTargets[i]) continue;
        if (_stepD[i] > 0) {
            _stepCurrent[i] += 1;
            digitalWriteFast(stepPins[i], HIGH);
            digitalWriteFast(stepPins[i], LOW);
            _stepD[i] = _stepD[i] - 2 * _stepCount;
        }
        _stepD[i] = _stepD[i] + 2 * _stepTargets[i];
    }
}

void initStepperPins() {
    for (int i = 0; i < N_MOTORS; i++) {
        pinMode(dirPins[i], OUTPUT);
        pinMode(stepPins[i], OUTPUT);
    }
}

bool steppersReady() {
    noInterrupts();
    bool stopped = true;
    for (int i = 0; i < N_MOTORS; i++) {
        if (_stepCurrent[i] < _stepTargets[i]) stopped = false;
    }
    interrupts();
    return stopped;
}

void startSteppers(long steps[], long time) {
    noInterrupts();
    _stepCount = time / _stepperTimerInterval;
    for (int i = 0; i < N_MOTORS; i++) {
        digitalWrite(dirPins[i], steps[i] > 0 ? HIGH : LOW);
        long nSteps = abs(steps[i]);
        _stepTargets[i] = nSteps;
        _stepCurrent[i] = 0;
        _stepD[i] = 2 * nSteps - time;
    }
    _stepperTimer.begin(_stepMotors, _stepperTimerInterval);
    interrupts();
}
