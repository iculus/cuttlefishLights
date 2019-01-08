#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 12
#define leds 22
#define rows 11
#define ultrasonic A0

uint16_t row = 0;
uint16_t col = 0;
uint16_t sz = 0;
uint16_t finger = 0;
uint8_t numFingers = 0;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(leds*rows, PIN, NEO_RGB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.



const int numReadings = 10;
int readings[numReadings];
int readIndex = 0;
int total = 0;
int average = 0;

void setup() {
  Serial.begin(9600);
  
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
  }
}

int incomingByte = 0;    // for incoming serial data
int a = 0;

struct Message1 {
  uint8_t a; //rows
  uint8_t b; //cols
  uint8_t c; //color
  uint8_t d; //brightness
  uint8_t e; //numFingers
  uint8_t f;
  uint8_t g;
  uint8_t h;
  uint8_t i;
  uint8_t j;
  uint8_t k;
  uint8_t l;
  uint8_t m;
  uint8_t n;
  uint8_t o;
  uint8_t p;
  uint8_t q;
  uint8_t r;
  uint8_t s;
  uint8_t t;
  uint8_t u;
  uint8_t v;
  uint8_t w;
  uint8_t x;
  uint8_t y;
  uint8_t z;
  uint8_t aa;
  uint8_t bb;
  uint8_t cc;
  uint8_t dd;
  
} __packed__;
static const size_t MSG_LEN = sizeof(struct Message1);

void loop() {
  struct Message1 msg1;
  static char payload[MSG_LEN];
  static size_t num_payload_chars = MSG_LEN + 1;

  total = total - readings[readIndex];
  readings[readIndex] = analogRead(ultrasonic);
  total = total + readings[readIndex];
  readIndex = readIndex +1;

  if (readIndex >= numReadings){
    readIndex = 0;
  }

  average = total/numReadings;
  //Serial.println(average);

  // send data only when you receive data:
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    // accumilate enough bytes
    // look for start bytes
    // 
    // pull out the payload
  
    if (num_payload_chars == MSG_LEN + 1) {
      if (incomingByte == 255) {
        num_payload_chars = 0;
      }
    } else if (num_payload_chars < MSG_LEN) {
      payload[num_payload_chars] = incomingByte;
      num_payload_chars++;
    } else if (num_payload_chars == MSG_LEN) {
      if (incomingByte == 254) {
        //process message
        memcpy(&msg1, payload, sizeof(msg1));
        handleMessage(msg1);
        num_payload_chars = MSG_LEN + 1;
      } else {
        num_payload_chars = MSG_LEN + 1;  // invalid packet, drop data
      }
    } else {
      //assert(false);
    }    
  }
}

void handleMessage(struct Message1 msg1){
  Serial.print("A");

  //left
  Serial.print(msg1.a, DEC); //pinky
  Serial.print(msg1.b, DEC); //pinky
  Serial.print(msg1.c, DEC); //pinky
  Serial.print(msg1.d, DEC); //ring
  Serial.print(msg1.e, DEC); //ring
  Serial.print(msg1.f, DEC); //ring
  Serial.print(msg1.g, DEC); //mid
  Serial.print(msg1.h, DEC); //mid
  Serial.print(msg1.i, DEC); //mid
  Serial.print(msg1.j, DEC); //ind
  Serial.print(msg1.k, DEC); //ind
  Serial.print(msg1.l, DEC); //ind
  Serial.print(msg1.m, DEC); //thmb
  Serial.print(msg1.n, DEC); //thmb
  Serial.print(msg1.o, DEC); //thmb

  //right
  Serial.print(msg1.p, DEC); //thmb
  Serial.print(msg1.q, DEC); //thmb
  Serial.print(msg1.r, DEC); //thmb
  Serial.print(msg1.s, DEC); //ind
  Serial.print(msg1.t, DEC); //ind
  Serial.print(msg1.u, DEC); //ind
  Serial.print(msg1.v, DEC); //mid
  Serial.print(msg1.w, DEC); //mid
  Serial.print(msg1.x, DEC); //mid
  Serial.print(msg1.y, DEC); //ring
  Serial.print(msg1.z, DEC); //ring
  Serial.print(msg1.aa, DEC);//ring
  Serial.print(msg1.bb, DEC);//pinky
  Serial.print(msg1.cc, DEC);//pinky
  Serial.print(msg1.dd, DEC);//pinky
  Serial.print("B");
}
  

