// Initialize a counter
volatile int event_counter = 0;

// The interrupt service routine (ISR)
void countEvent() { event_counter++; }

void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT_PULLUP); // Using internal pull-up resistor 
  //I have also added 10KOhm Series With the meter

  // Attach the interrupt to pin 2 (interrupt 0), triggering on falling edge
  attachInterrupt(digitalPinToInterrupt(2), countEvent, FALLING);
}

void loop() {
Serial.println(event_counter);
delay(1000);
}