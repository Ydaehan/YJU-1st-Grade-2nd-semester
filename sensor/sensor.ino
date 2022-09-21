/*
 제목    : 초음파센서로 거리 측정하기
 내용   : 초음파센서로부터 10cm 이내로 물체가 감지되었을때 LED가 켜지도록 만들어 봅시다.
 */

//  int duration1 = 0; // left
//  int duration2 = 0; // middle
//  int duration3 = 0; // right
  
// 실행시 가장 먼저 호출되는 함수이며, 최초 1회만 실행됩니다.
// 변수를 선언하거나 초기화를 위한 코드를 포함합니다.
void setup() {
  // 초음파센서의 동작 상태를 확인하기 위하여 시리얼 통신을 설정합니다. (전송속도 9600bps)
  Serial.begin(9600);
  //초음파 송신부-> OUTPUT, 초음파 수신부 -> INPUT,  LED핀 -> OUTPUT

  // left
  pinMode(3, OUTPUT);
  pinMode(2, INPUT);
  
  // middle
  pinMode(5, OUTPUT);
  pinMode(4, INPUT);

  // right
  pinMode(7, OUTPUT);
  pinMode(6, INPUT);

}
 
// setup() 함수가 호출된 이후, loop() 함수가 호출되며,
// 블록 안의 코드를 무한히 반복 실행됩니다.
void loop() {
  digitalWrite(3, LOW);
  digitalWrite(2, LOW);
  delayMicroseconds(2);
  digitalWrite(3, HIGH);
  delayMicroseconds(10);
  digitalWrite(3, LOW);
  unsigned long duration1 = pulseIn(2, HIGH);

  digitalWrite(5, LOW);
  digitalWrite(4, LOW);
  delayMicroseconds(2);
  digitalWrite(5, HIGH);
  delayMicroseconds(10);
  digitalWrite(5, LOW);
  unsigned long duration2 = pulseIn(4, HIGH);

  digitalWrite(7, LOW);
  digitalWrite(6, LOW);
  delayMicroseconds(2);
  digitalWrite(7, HIGH);
  delayMicroseconds(10);
  digitalWrite(7, LOW);
  unsigned long duration3 = pulseIn(6, HIGH);
 
  // 초음파의 속도는 초당 340미터를 이동하거나, 29마이크로초 당 1센치를 이동합니다.
  // 따라서, 초음파의 이동 거리 = duration(왕복에 걸린시간) / 29 / 2 입니다.
  float distance1 = duration1 / 29.0 / 2.0;
  float distance2 = duration2 / 29.0 / 2.0;
  float distance3 = duration3 / 29.0 / 2.0;
  // 측정된 거리 값를 시리얼 모니터에 출력합니다.
  
  Serial.print("left : ");
  Serial.print(distance1);
  Serial.print("cm ");

  Serial.print("middle : ");
  Serial.print(distance2);
  Serial.print("cm ");

  Serial.print("right : ");
  Serial.print(distance3);
  Serial.println("cm");
  delay(500);
}
