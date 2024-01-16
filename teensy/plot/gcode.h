#include <Arduino.h>

typedef struct {
  double feed;
  double pos[2];

  double servoPos;
} Command;

Command command = { 1000, { 0, 0 }, 0 };

const int BUFFER_LEN = 2;
Command commandBuffer[BUFFER_LEN];
int commandBack = 0;
int commandsInBuffer = 0;

char serialBuffer[1024];
int serialLen = 0;

void parseCoord(String* str, char chr, double* dest) {
  int idx = str->indexOf(chr);
  if (idx != -1) {
    *dest = atof(str->substring(idx+1).c_str());
  }
}

bool parseCommand(String* line) {
  if (!line->length()) return false;

  bool ok = false;

  if (line->startsWith("M280")) {
    parseCoord(line, 'S', &command.servoPos);
    ok = true;
  }
  if (line->startsWith("G0") || line->startsWith("G1")) {
    parseCoord(line, 'X', &command.pos[0]);
    parseCoord(line, 'Y', &command.pos[1]);
    parseCoord(line, 'F', &command.feed);
    ok = true;
  }

  if (ok) {
    return true;
  }

  Serial.println(String("// Unknown command: ").concat(*line));
  return false;
}

bool readInput() {
  if (commandsInBuffer < BUFFER_LEN && Serial.available() > 0) {
    char ch = Serial.read();
    if (ch == -1) {
      return false;
    }

    if (ch == '\n') {
       serialBuffer[serialLen] = '\0';
       serialLen = 0;

       String line = String(serialBuffer);
       line.trim();
       if (parseCommand(&line)) {
         commandBuffer[(commandBack + commandsInBuffer) % BUFFER_LEN] = command;
         commandsInBuffer += 1;
         return true;
       }
    } else {
       serialBuffer[serialLen] = ch;
       serialLen++;
    }
  }
  return false;
}
