const int leftPin = 13;
const int rightPin = 12;
int incomingByte;

void setup() {
  Serial.begin(9600);
  pinMode(leftPin, OUTPUT);
  pinMode(rightPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'L') {
      digitalWrite(leftPin, HIGH);
    }
    if (incomingByte == 'R') {
      digitalWrite(rightPin, HIGH);
    }
    if (incomingByte == 'D') {
      digitalWrite(rightPin, LOW);
      digitalWrite(leftPin, LOW);
    }
  }
}
