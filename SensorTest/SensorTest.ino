#define ultrasonic A1
#define slider A0
#define button A2
#define cpuPower A5
#define interrupt 4
#define colorLED 5

void setup() {
  // put your setup code here, to run once:
  pinMode(ultrasonic, INPUT);
  pinMode(slider, INPUT);
  pinMode(button, INPUT_PULLUP);
  pinMode(cpuPower, INPUT);

  digitalWrite(colorLED, LOW);
  
  Serial.begin(9600);
}

void loop() {
  digitalWrite(colorLED, HIGH);
  int ultrasonicReading = analogRead(ultrasonic);
  int sliderReading = analogRead(slider);
  int buttonReading = analogRead(button);
  int cpuReading = analogRead(cpuPower);
  int mappedSliderReading = map(sliderReading,0,1024,0,255);
  Serial.print(ultrasonicReading);
  Serial.print('\t');
  Serial.print(mappedSliderReading);
  Serial.print('\t');
  Serial.print(buttonReading);
  Serial.print('\t');
  Serial.print(cpuReading);
  Serial.print('\n');

}
