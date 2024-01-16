#include <Arduino.h>

// To use, include this header file, and call initStepperPins at setup
// Then you can call startSteppers whenever steppersReady() is true

const int N_MOTORS = 2;
const int dirPins[] = { 13, 15 };
const int stepPins[] = { 14, 16 };

IntervalTimer _stepperTimer;
const int _stepperTimerInterval = 2;

volatile long _stepCount = 0;
volatile long _stepTargets[] = { 0, 0 };
volatile long _stepCurrent[] = { 0, 0 };
volatile long _stepD[] = { 0, 0 }; // For bresenham's line algorithm
volatile long _waitTicks = 0;

volatile int _u = 1;
volatile int _v = 1;
int rand() {
    _v = 36969*(_v & 65535) + (_v >> 16);
    _u = 18000*(_u & 65535) + (_u >> 16);
    return (_v << 16) + (_u & 65535);
}

void _stepMotors() {
    if (_waitTicks > 0) {
        _waitTicks--;
	return;
    }
    _waitTicks = 16 + rand() % 3;
    // _waitTicks = 20;

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
    _stepperTimer.begin(_stepMotors, _stepperTimerInterval);
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
    _stepCount = time / _stepperTimerInterval / 17;
    for (int i = 0; i < N_MOTORS; i++) {
        digitalWriteFast(dirPins[i], (steps[i] > 0) ? HIGH : LOW);
        long nSteps = abs(steps[i]);
        _stepTargets[i] = nSteps;
        _stepCurrent[i] = 0;
        _stepD[i] = 2 * nSteps - _stepCount;
    }
    _waitTicks = 0;
    interrupts();
}
