#define motorPin 11
#define buttonPin 7

void setup() {
  pinMode(motorPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  analogWrite(motorPin, 0);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    analogWrite(motorPin, 200);   // pressed = fan ON
  } else {
    analogWrite(motorPin, 0);     // not pressed = fan OFF
  }
}