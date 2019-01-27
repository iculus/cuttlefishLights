#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#include "colors.h"
#include "message.h"

#define ultrasonic A1
#define slider A0

uint16_t row = 0;
uint16_t col = 0;
uint16_t sz = 0;
uint16_t finger = 0;
uint8_t numFingers = 0;



const int numReadings = 6;
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



bool serAvail = false;
bool closeToIt = false;
int threshold = 100;
int i = 0;
int startTime = millis();
int checkTime = millis();

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

  if (Serial.available() > 0)  {serAvail = true;}
  if (Serial.available() == 0) {serAvail = false;}
  if (average > threshold )    {closeToIt = false;}
  if (average <= threshold )   {closeToIt = true;}

  bool condition = serAvail;
  //bool condition = true;

  if (condition) {
    startTime = millis();
    checkTime = millis();
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
  else if(not condition) {
    checkTime = millis();
    row = random(0,rows);
    col = random(0,leds);
    sz = random(1,4+1);
    uint8_t seqLen = 22*11;

    if (checkTime-startTime>=1000){
      startTime = checkTime - 1000; //to prevent overflow condition
      DrawCircle(row,col,0,0,sz); // row,col,color,wait,size(1=small,4=large)
    }
    //DrawLines( seq, seqLen, strip.Color(0,0,255), 40, 4); //onOff vals, len, color, brightness
  }
}

uint32_t thisColor;

uint8_t ZIG(uint8_t in, uint8_t width){
  int j = 0; 
  int maths = in/width;
  if(maths%2){
    j = (width-1)+(width*maths) - (in-(width*maths));
  }
  else {j = in;}
  return j;
}

void DrawLines (int sequence[], uint8_t arLen, uint32_t color, uint8_t brightness, uint8_t nums){
  for (int i = 0; i < arLen; i++){
    /*
    int j = 0; 
    int maths = i/22;
    if(maths%2){
      j = 21+(22*maths) - (i-(22*maths));
    }
    else {j = i;}
    */
    uint8_t j = ZIG(i,22);
    
    if (sequence[i] > 0){
      if (sequence[i] == 0){thisColor = OFF;}
      if (sequence[i] == 1){thisColor = PURPLE;}
      if (sequence[i] == 2){thisColor = GREEN;}
      if (sequence[i] == 3){thisColor = TEAL;}
      if (sequence[i] == 4){thisColor = RED;}
      if (sequence[i] == 5){thisColor = YELLOW;}
      if (sequence[i] == 6){thisColor = FUCHA;}
      if (sequence[i] == 7){thisColor = BLUE;}
      if (sequence[i] == 8){thisColor = ORANGE;}
      if (sequence[i] == 9){thisColor = WHITE;}
      if (sequence[i] == 10){thisColor = NEW;}
      strip.setPixelColor(j, thisColor);
    }
  }
  if (nums != 5){ strip.setBrightness(brightness); }
  if (nums == 5){ strip.setBrightness(255); }
  //strip.show();
  if (nums == 5 or nums ==0){
    for (int k=0; k<strip.numPixels(); k++){
      uint8_t L = ZIG(k,22);
      if (sequence[k] == 0){
        strip.setPixelColor(L, strip.Color(0,0,0));
      }
    }
  }
  strip.show();
}

void handleMessage(struct Message1 msg1){

  uint8_t seqLen = 22*11;

  uint8_t numFing = msg1.bit242;

  uint8_t brights = msg1.bit243;

  int seq[] = {  msg1.bit0,  msg1.bit1,  msg1.bit2,  msg1.bit3,  msg1.bit4,  msg1.bit5,  msg1.bit6,  msg1.bit7,  msg1.bit8,  msg1.bit9,  msg1.bit10, msg1.bit11, msg1.bit12, msg1.bit13, msg1.bit14, msg1.bit15, msg1.bit16, msg1.bit17, msg1.bit18, msg1.bit19, msg1.bit20, msg1.bit21,
      msg1.bit22, msg1.bit23, msg1.bit24, msg1.bit25, msg1.bit26, msg1.bit27, msg1.bit28, msg1.bit29, msg1.bit30, msg1.bit31, msg1.bit32, msg1.bit33, msg1.bit34, msg1.bit35, msg1.bit36, msg1.bit37, msg1.bit38, msg1.bit39, msg1.bit40, msg1.bit41, msg1.bit42, msg1.bit43,
      msg1.bit44, msg1.bit45, msg1.bit46, msg1.bit47, msg1.bit48, msg1.bit49, msg1.bit50, msg1.bit51, msg1.bit52, msg1.bit53, msg1.bit54, msg1.bit55, msg1.bit56, msg1.bit57, msg1.bit58, msg1.bit59, msg1.bit60, msg1.bit61, msg1.bit62, msg1.bit63, msg1.bit64, msg1.bit65,
      msg1.bit66, msg1.bit67, msg1.bit68, msg1.bit69, msg1.bit70, msg1.bit71, msg1.bit72, msg1.bit73, msg1.bit74, msg1.bit75, msg1.bit76, msg1.bit77, msg1.bit78, msg1.bit79, msg1.bit80, msg1.bit81, msg1.bit82, msg1.bit83, msg1.bit84, msg1.bit85, msg1.bit86, msg1.bit87,
      msg1.bit88, msg1.bit89, msg1.bit90, msg1.bit91, msg1.bit92, msg1.bit93, msg1.bit94, msg1.bit95, msg1.bit96, msg1.bit97, msg1.bit98, msg1.bit99, msg1.bit100,  msg1.bit101,  msg1.bit102,  msg1.bit103,  msg1.bit104,  msg1.bit105,  msg1.bit106,  msg1.bit107,  msg1.bit108,  msg1.bit109,
      msg1.bit110,  msg1.bit111,  msg1.bit112,  msg1.bit113,  msg1.bit114,  msg1.bit115,  msg1.bit116,  msg1.bit117,  msg1.bit118,  msg1.bit119,  msg1.bit120,  msg1.bit121,  msg1.bit122,  msg1.bit123,  msg1.bit124,  msg1.bit125,  msg1.bit126,  msg1.bit127,  msg1.bit128,  msg1.bit129,  msg1.bit130,  msg1.bit131,
      msg1.bit132,  msg1.bit133,  msg1.bit134,  msg1.bit135,  msg1.bit136,  msg1.bit137,  msg1.bit138,  msg1.bit139,  msg1.bit140,  msg1.bit141,  msg1.bit142,  msg1.bit143,  msg1.bit144,  msg1.bit145,  msg1.bit146,  msg1.bit147,  msg1.bit148,  msg1.bit149,  msg1.bit150,  msg1.bit151,  msg1.bit152,  msg1.bit153,
      msg1.bit154,  msg1.bit155,  msg1.bit156,  msg1.bit157,  msg1.bit158,  msg1.bit159,  msg1.bit160,  msg1.bit161,  msg1.bit162,  msg1.bit163,  msg1.bit164,  msg1.bit165,  msg1.bit166,  msg1.bit167,  msg1.bit168,  msg1.bit169,  msg1.bit170,  msg1.bit171,  msg1.bit172,  msg1.bit173,  msg1.bit174,  msg1.bit175,
      msg1.bit176,  msg1.bit177,  msg1.bit178,  msg1.bit179,  msg1.bit180,  msg1.bit181,  msg1.bit182,  msg1.bit183,  msg1.bit184,  msg1.bit185,  msg1.bit186,  msg1.bit187,  msg1.bit188,  msg1.bit189,  msg1.bit190,  msg1.bit191,  msg1.bit192,  msg1.bit193,  msg1.bit194,  msg1.bit195,  msg1.bit196,  msg1.bit197,
      msg1.bit198,  msg1.bit199,  msg1.bit200,  msg1.bit201,  msg1.bit202,  msg1.bit203,  msg1.bit204,  msg1.bit205,  msg1.bit206,  msg1.bit207,  msg1.bit208,  msg1.bit209,  msg1.bit210,  msg1.bit211,  msg1.bit212,  msg1.bit213,  msg1.bit214,  msg1.bit215,  msg1.bit216,  msg1.bit217,  msg1.bit218,  msg1.bit219,
      msg1.bit220,  msg1.bit221,  msg1.bit222,  msg1.bit223,  msg1.bit224,  msg1.bit225,  msg1.bit226,  msg1.bit227,  msg1.bit228,  msg1.bit229,  msg1.bit230,  msg1.bit231,  msg1.bit232,  msg1.bit233,  msg1.bit234,  msg1.bit235,  msg1.bit236,  msg1.bit237,  msg1.bit238,  msg1.bit239,  msg1.bit240,  msg1.bit241};
  //Serial.println(msg1, DEC)
  //Serial.print(msg1.a, DEC);
  //Serial.print(msg1.b, DEC);
  //Serial.print(msg1.c, DEC);
  //Serial.println(msg1.d, DEC);
  //Serial.print(msg1.e,DEC);
  //row = random(0,rows);
  //col = random(0,leds);
  //sz = random(1,4+1);
  //sz = 1;
  //row = int(msg1.a);
  //col = int(msg1.b);
  //finger = int(msg1.c);
  //numFingers = int(msg1.e);

  //Serial.print(numFingers);

  //DrawCircle(row,col,0,1,sz); // row,col,color,wait,size(1=small,4=large)
  //DrawDot(row,col,finger,1,255,numFingers); // row,col,color,wait,brightness

  DrawLines( seq, seqLen, strip.Color(0,0,255), brights, numFing); //onOff vals, len, color, brightness

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

#define ARRAY_LEN(a)    (sizeof(a) / sizeof(a[0]))
/*
uint32_t RED = strip.Color(0,255,0);
uint32_t ORANGE = strip.Color(100,255,0);
uint32_t YELLOW = strip.Color(255,255,0);
uint32_t GREEN = strip.Color(255,0,0);
uint32_t TEAL = strip.Color(255,0,255);
uint32_t BLUE = strip.Color(0,0,255);
uint32_t FUCHA = strip.Color(0,255,100);
uint32_t PURPLE = strip.Color(0,170,255);
uint32_t WHITE = strip.Color(255,255,255);
uint32_t OFF = strip.Color(0,0,0);
*/

//uint32_t thisColor;

void DrawCircle(uint16_t row, uint16_t col, uint32_t color, uint8_t wait, uint16_t condition) {
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
    if (condition >= 1) {addressShape(xx1,yy1,row,col,ARRAY_LEN(xx1),YELLOW);}
    strip.setBrightness( 255/50 * (50-abs(50-b)) ); //sets the triangle
    strip.show();
    delay(wait);
  }
}

void DrawDot(uint16_t row, uint16_t col, uint32_t color, uint8_t wait, uint16_t brightness, uint8_t numFingers) {
  static int xx1[] = {0};
  static int yy1[] = {0};

  if (numFingers == 1) {thisColor = FUCHA;}
  if (numFingers == 5) {thisColor = PURPLE;}
  if (numFingers == 3) {thisColor = BLUE;}
  if (numFingers == 4) {thisColor = ORANGE;}
  if (numFingers == 2) {thisColor = OFF;}
  if (numFingers == 6) {thisColor = GREEN;}
  if (numFingers == 7) {thisColor = YELLOW;}
  
  addressShape(xx1,yy1,row,col,ARRAY_LEN(xx1),thisColor);
  strip.setBrightness(brightness);
  strip.show();
  delay(wait);
  if (numFingers == 10) {
    for(int i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, strip.Color(0,0,0));
    }  
  }
  strip.show();
  delay(wait);
}

void addressShape(int* xArray, int* yArray, uint16_t thisrow, uint16_t thiscol, uint16_t arraylen,uint32_t c){
  for (int dot=0; dot < arraylen; dot++) {
    if ((xArray[dot]+thisrow)>=0 && (yArray[dot]+thiscol)>=0 && (xArray[dot]+thisrow)<rows && (yArray[dot]+thiscol)<leds) {
      SetPixelMatrix(xArray[dot]+thisrow,yArray[dot]+thiscol, c);
    }
  }
}
