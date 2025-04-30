#include <Arduino.h>

const int relayPin = 7; // Change to your relay pin

void setup() {
    Serial.begin(9600);
    pinMode(relayPin, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        char received = Serial.read();
        
        if (received == '1') {
            digitalWrite(relayPin, LOW);
            Serial.println("Relay turned ON");
        } else if (received == '0') {
            digitalWrite(relayPin, HIGH);
            Serial.println("Relay turned OFF");
        }
    }
}
