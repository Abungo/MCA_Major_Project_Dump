void setup() {
  // Initialize the serial communication at 9600 baud rate
  Serial.begin(9600);

  // Set the analog pin A5 as input (optional, as analogRead sets the pin mode automatically)
  pinMode(A5, INPUT);
}

void loop() {
  // Read the analog value from pin A5
  int analogValue = analogRead(A5);

  // Print the analog value to the serial monitor
  Serial.print("Analog value at A5: ");
  Serial.println(analogValue);

  // Wait for 500 milliseconds before the next read
  delay(500);
}