#include <Servo.h>

const int servoPin = 17;

Servo servo;

void setup() {
    servo.attach(servoPin);
}

void loop() {
    servo.write(0);
    delay(1000);
    servo.write(30);
    delay(1000);
}
