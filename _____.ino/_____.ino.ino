#include <ArduinoJson.h>

int duration1 = 0; // left
int duration2 = 0; // mid
int duration3 = 0; // right

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // left
  pinMode(3, OUTPUT); // TRIG
  pinMode(2, INPUT);  // ECHO

  // middle
  pinMode(5, OUTPUT); // TRIG
  pinMode(4, INPUT);  // ECHO
  
  // right
  pinMode(7, OUTPUT); // TRIG
  pinMode(6, INPUT);  // ECHO
}

void loop() {
  // put your main code here, to run repeatedly:
  StaticJsonDocument<200> doc;
  String json;

  digitalWrite(3,LOW);
  delayMicroseconds(2);
  digitalWrite(3,HIGH);
  delayMicroseconds(10);
  digitalWrite(3,LOW);
  duration1 = pulseIn(2, HIGH);
  
  digitalWrite(5,LOW);
  delayMicroseconds(2);
  digitalWrite(5,HIGH);
  delayMicroseconds(10);
  digitalWrite(5,LOW);
  duration2 = pulseIn(4, HIGH);

  digitalWrite(7,LOW);
  delayMicroseconds(2);
  digitalWrite(7,HIGH);
  delayMicroseconds(10);
  digitalWrite(7,LOW);
  duration3 = pulseIn(6, HIGH);

  doc["left"]   = duration1 / 29 / 2;
  doc["middle"] = duration2 / 29 / 2;
  doc["right"]  = duration3 / 29 / 2;

  serializeJson(doc, json);
  Serial.println(json);
  delay(1000);
}
