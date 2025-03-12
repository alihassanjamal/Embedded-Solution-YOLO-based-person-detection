
#include <LiquidCrystal_I2C.h>  // Include the LiquidCrystal library
#include <Wire.h>
const int buzzerPin = 10;  // Define the pin for the buzzer
/*const int rs = 12;         // LCD RS pin
const int en = 11;         // LCD enable pin
const int d4 = 5;          // LCD data pin 4
const int d5 = 4;          // LCD data pin 5
const int d6 = 3;          // LCD data pin 6
const int d7 = 2;          // LCD data pin 7*/
LiquidCrystal_I2C lcd(0x27,16,2);  // Initialize the LCD with the pins

const int ledPin = 13;
void setup() {
  Serial.begin(230400);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buzzerPin, OUTPUT);  // Set the buzzer pin as an output
  lcd.init();
  lcd.backlight();
  lcd.clear();       // Clear the LCD screen
}

void loop() {
  if (Serial.available() > 0) {
    char NoofPeople_string = Serial.read();
    int NoofPeople = asciiToInt(NoofPeople_string);

     // Display the number of people on the LCD screen
    lcd.clear();  // Clear the LCD screen
    lcd.setCursor(0, 0);  // Set the cursor to the first row
    lcd.print("People Detected:");
    lcd.setCursor(0, 1);  // Set the cursor to the second row
    lcd.print(NoofPeople);
    
    // If number of people detected is greater than 0, blink the LED
    if (NoofPeople > 0) {
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(buzzerPin, HIGH);
    }
    else {
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(buzzerPin, LOW);
    }
    
  }
}

int asciiToInt(char asciiChar) {
  // Subtract ASCII value of '0' from the ASCII character to get the integer value
  return asciiChar - '0';
}
