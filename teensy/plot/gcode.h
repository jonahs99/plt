#include <Arduino.h>

typedef struct {
  float feed;
  float pos[2];
} Command;

Command command = { 1000, { 0, 0 } };

const int BUFFER_LEN = 16;
Command commandBuffer[BUFFER_LEN];
int commandBack = 0;
int commandsInBuffer = 0;

void parseCoord(String* str, char chr, float* dest) {
  int idx = str->indexOf(chr);
  if (idx != -1) {
    *dest = str->substring(idx+1).toFloat();
  }
}

bool parseCommand(String* line) {
  if (!line->length()) return false;
  if (line->startsWith("G0") || line->startsWith("G1")) {
    parseCoord(line, 'X', &command.pos[0]);
    parseCoord(line, 'Y', &command.pos[1]);
    parseCoord(line, 'F', &command.feed);
    return true;
  }

  Serial.println(String("// Unknown command: ").concat(*line));
  return false;
}

bool readInput() {
  if (commandsInBuffer < BUFFER_LEN-1 && Serial.available() > 0) {
    String line = Serial.readStringUntil('\n');
    line.trim();
    if (parseCommand(&line)) {
      memcpy(&commandBuffer[(commandBack + commandsInBuffer) % BUFFER_LEN], &command, sizeof(command));
      commandsInBuffer += 1;
      return true;
    }
    Serial.println("ok");
  }
  return false;
}
