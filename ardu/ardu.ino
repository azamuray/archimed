const int leftPin = 13;
const int rightPin = 12;

#define A 3
#define B 4
#define C 5
#define D 6
#define NUMBER_OF_STEPS_PER_REV 512

void write(int a,int b,int c,int d){
  digitalWrite(A,a);
  digitalWrite(B,b);
  digitalWrite(C,c);
  digitalWrite(D,d);
}

void goLeft(){
  write(1,0,0,0);
  delay(5);
  write(1,1,0,0);
  delay(5);
  write(0,1,0,0);
  delay(5);
  write(0,1,1,0);
  delay(5);
  write(0,0,1,0);
  delay(5);
  write(0,0,1,1);
  delay(5);
  write(0,0,0,1);
  delay(5);
  write(1,0,0,1);
  delay(5);
}

void goRight(){
  write(1,0,0,1);
  delay(5);
  write(0,0,0,1);
  delay(5);
  write(0,0,1,1);
  delay(5);
  write(0,0,1,0);
  delay(5);
  write(0,1,1,0);
  delay(5);
  write(0,1,0,0);
  delay(5);
  write(1,1,0,0);
  delay(5);
  write(1,0,0,0);
  delay(5);
}
int incomingByte;

void setup() {
  Serial.begin(9600);
  pinMode(leftPin, OUTPUT);
  pinMode(rightPin, OUTPUT);

  // Setup stepper driver
  pinMode(A,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(C,OUTPUT);
  pinMode(D,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'L') {
      digitalWrite(leftPin, HIGH);
      goLeft();
    }
    if (incomingByte == 'R') {
      digitalWrite(rightPin, HIGH);
      goRight();
    }
    if (incomingByte == 'D') {
      digitalWrite(rightPin, LOW);
      digitalWrite(leftPin, LOW);
    }
  }
}
