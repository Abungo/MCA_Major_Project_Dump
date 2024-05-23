#include <SPI.h>
#include <RF24.h>

// Define the CE and CSN pins for the NRF24L01 module
#define CE_PIN   9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN); // Create a radio object

const byte address[6] = "00001"; // Address of the transmitter and receiver

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize the NRF24L01 module
  radio.begin();
  radio.openWritingPipe(address); // Set the address for writing data
}

void loop() {
  // Read the analog value from pin A5
  int analogValue = analogRead(A5);

  // Print the analog value to the serial monitor
  Serial.print("Analog value at A5: ");
  Serial.println(analogValue);

  // Send the analog value via NRF24L01
  radio.write(&analogValue, sizeof(analogValue));

  // Wait for 500 milliseconds before the next read
  delay(500);
}