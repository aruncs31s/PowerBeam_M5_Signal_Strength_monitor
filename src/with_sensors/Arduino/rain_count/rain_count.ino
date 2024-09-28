// Initialize a counter
volatile int eventCounter = 0;

void countEvent() { eventCounter++; }

void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT_PULLUP); 
  attachInterrupt(digitalPinToInterrupt(2), countEvent, FALLING);
}

void loop() {
  Serial.print("Event count: ");
  Serial.println(eventCounter);

  delay(500);
}
