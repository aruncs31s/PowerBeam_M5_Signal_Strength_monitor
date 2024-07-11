// Initialize a counter
volatile int eventCounter = 0;

// The interrupt service routine (ISR)
void countEvent() { eventCounter++; }

void setup() {
  // Start serial communication for debugging
  Serial.begin(9600);

  // Configure the button pin as input
  pinMode(2, INPUT_PULLUP); // Using internal pull-up resistor

  // Attach the interrupt to pin 2 (interrupt 0), triggering on falling edge
  attachInterrupt(digitalPinToInterrupt(2), countEvent, FALLING);
}

void loop() {
  // Print the counter value
  Serial.print("Event count: ");
  Serial.println(eventCounter);

  // Small delay to reduce serial output flooding
  delay(500);
}
