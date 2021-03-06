#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 12
#define leds 22
#define rows 11

uint16_t row = 0;
uint16_t col = 0;
uint16_t sz = 0;

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(leds*rows, PIN, NEO_RGB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  Serial.begin(9600);
  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
  #if defined (__AVR_ATtiny85__)
    if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif
  // End of trinket special code

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

int incomingByte = 0;    // for incoming serial data
int a = 0;

struct Message1 {
  uint8_t a;
  uint8_t b;
  uint8_t c;
  uint8_t d;
} __packed__;
static const size_t MSG_LEN = sizeof(struct Message1);

void loop() {
    struct Message1 msg1;
  static char payload[MSG_LEN];
  static size_t num_payload_chars = MSG_LEN + 1;

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
  Serial.print(msg1.a, DEC);
  Serial.print(msg1.b, DEC);
  Serial.print(msg1.c, DEC);
  Serial.println(msg1.d, DEC);

  //row = random(0,rows);
  //col = random(0,leds);
  sz = random(1,4+1);
  row = int(msg1.a);
  col = int(msg1.b);

  DrawCircle(row,col,0,1,sz); // row,col,color,wait,size(1=small,4=large)
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void colorFill(uint32_t c) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
  }
  strip.show();
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
      for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

uint16_t Wrap(uint16_t n, uint16_t len) {
  return ((n % len) + len) % len;
}

uint16_t TransformMatrix(uint16_t row, uint16_t col) {
  // 0,0 is bottom left
  //row = Wrap(row,rows);
  //col = Wrap(col,leds);
  uint16_t ColAdder;
  if (row%2 == 1) {
    ColAdder = leds-col-1;
  }
  else {
    ColAdder = col;
  }
  return row*leds + ColAdder;
}

void SetPixelMatrix(uint16_t row, uint16_t col, uint32_t c) {
  uint16_t i = TransformMatrix(row, col);
  strip.setPixelColor(i, c);
}

void DiagonalFader(uint16_t row, uint16_t col, uint32_t c, uint8_t len, uint8_t wait) {
  for (int n = 0; n < len*2; n++) {
    uint32_t brightness, setrow, setcol;
    if (n==0) {
      brightness = 0;
    }
    else {
      brightness = 1;
    }
    setrow = row+n;
    setcol = col+n;
    
    Serial.print("r1 ");
    Serial.println(setrow);
    Serial.print("c1 ");
    Serial.println(setcol);

    setcol = (setcol - (setrow/rows)*(rows-1)) % leds;
    setrow = setrow % rows;

    Serial.print("r2 ");
    Serial.println(setrow);
    Serial.print("c2 ");
    Serial.println(setcol);
    
    SetPixelMatrix(setrow, setcol, strip.Color(0, 0, 255*brightness));
  }
  strip.show();
  delay(wait);
}

#define ARRAY_LEN(a)    (sizeof(a) / sizeof(a[0]))

void DrawCircle(uint16_t row, uint16_t col, uint32_t c, uint8_t wait, uint16_t condition) {
  static int xx4[] = {-3,-3,-2,-1,0,1,2,3,3,3,2,1,0,-1,-2,-3};
  static int yy4[] = {0,1,2,3,3,3,2,1,0,-1,-2,-3,-3,-3,-2,-1};
  static int xx3[] = {-1,0,1,2,2,2,1,0,-1,-2,-2,-2};
  static int yy3[] = {2,2,2,1,0,-1,-2,-2,-2,-1,0,1};
  static int xx2[] = {-1,-1,0,1,1,1,0,-1};
  static int yy2[] = {0,1,1,1,0,-1,-1,-1};
  static int xx1[] = {0};
  static int yy1[] = {0};
  
  for (int b = 0; b <= 100; b++) {
    if (condition >= 4) {addressShape(xx4,yy4,row,col,ARRAY_LEN(xx4),strip.Color(0,1*(50-abs(50-b)),1*(50-abs(50-b))));}
    if (condition >= 3) {addressShape(xx3,yy3,row,col,ARRAY_LEN(xx3),strip.Color(0,0,2*(50-abs(50-b))));}
    if (condition >= 2) {addressShape(xx2,yy2,row,col,ARRAY_LEN(xx2),strip.Color(0,1*(50-abs(50-b)),0));}
    if (condition >= 1) {addressShape(xx1,yy1,row,col,ARRAY_LEN(xx1),strip.Color(4*(50-abs(50-b)),4*(50-abs(50-b)),0));}
    strip.show();
    delay(wait);
  }
}

void addressShape(int* xArray, int* yArray, uint16_t thisrow, uint16_t thiscol, uint16_t arraylen,uint32_t c){
  for (int dot=0; dot < arraylen; dot++) {
    if ((xArray[dot]+thisrow)>=0 && (yArray[dot]+thiscol)>=0 && (xArray[dot]+thisrow)<rows && (yArray[dot]+thiscol)<leds) {
      SetPixelMatrix(xArray[dot]+thisrow,yArray[dot]+thiscol, c);
    }
  }
}

