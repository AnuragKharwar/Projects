#include <SPI.h> //A Serial Peripheral Interface (SPI) bus is a system for serial communication

#define SS_PIN 10
#define RST_PIN 9
#define LED_G 8 // define green LED pin
#define LED_R 7 // define red LED
#define In1 2   // motor pin for door locking mechanism
#define In2 3
#define fan 5
#define light 6
#define lamp 4

void setup()
{
  Serial.begin(9600); // Initiate a serial communication

  pinMode(fan, OUTPUT);   // for fan control
  pinMode(light, OUTPUT); // for light control
  pinMode(lamp, OUTPUT);  // for lamp control
  pinMode(LED_G, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(In1, OUTPUT); // for door control which uses motor driver board input one
  pinMode(In2, OUTPUT); // for motor driver board input
}
void loop()

{

  // bluetooth setup
  String val = Serial.readString();
  Serial.println(val);
  if (val == "fan on")
  {
    digitalWrite(fan, HIGH);
  }
  if (val == "fan off")
  {
    digitalWrite(fan, LOW);
  }
  if (val == "light on")
  {
    digitalWrite(light, HIGH);
  }
  if (val == "light off")
  {
    digitalWrite(light, LOW);
  }
  if (val == "lamp on")
  {
    digitalWrite(lamp, HIGH);
  }
  if (val == "lamp off")
  {
    digitalWrite(lamp, LOW);
  }
  if (val == "all off")
  {
    digitalWrite(light, LOW);
    digitalWrite(fan, LOW);
    digitalWrite(lamp, LOW);
  }
  if (val == "all Of")
  {
    digitalWrite(light, LOW);
    digitalWrite(fan, LOW);
    digitalWrite(lamp, LOW);
  }
  if (val == "all on")
  {
    digitalWrite(fan, HIGH);
    digitalWrite(light, HIGH);
    digitalWrite(lamp, HIGH);
  }

  if (val == "unlock")
  {
    Serial.println("unlock");
    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    delay(1000);
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
  }
  if (val == "lock")
  {
    digitalWrite(In2, HIGH);
    digitalWrite(In1, LOW);
    delay(1000);
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
  }
}
