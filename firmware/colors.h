#define leds 22
#define rows 11
#define PIN 6

uint32_t thisColor;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(leds*rows, PIN, NEO_RGB + NEO_KHZ800);

uint32_t RED_0 = strip.Color(0,0,0);
uint32_t RED_1 = strip.Color(0,0,0);
uint32_t RED_2 = strip.Color(0,2,0);
uint32_t RED_3 = strip.Color(0,9,0);
uint32_t RED_4 = strip.Color(0,22,0);
uint32_t RED_5 = strip.Color(0,43,0);
uint32_t RED_6 = strip.Color(0,75,0);
uint32_t RED_7 = strip.Color(0,119,0);
uint32_t RED_8 = strip.Color(0,179,0);
uint32_t RED_9 = strip.Color(0,255,0);


uint32_t ORANGE_0 = strip.Color(0,0,0);
uint32_t ORANGE_1 = strip.Color(0,0,0);
uint32_t ORANGE_2 = strip.Color(1,2,0);
uint32_t ORANGE_3 = strip.Color(3,9,0);
uint32_t ORANGE_4 = strip.Color(8,22,0);
uint32_t ORANGE_5 = strip.Color(17,43,0);
uint32_t ORANGE_6 = strip.Color(29,75,0);
uint32_t ORANGE_7 = strip.Color(47,119,0);
uint32_t ORANGE_8 = strip.Color(70,179,0);
uint32_t ORANGE_9 = strip.Color(100,255,0);


uint32_t YELLOW_0 = strip.Color(0,0,0);
uint32_t YELLOW_1 = strip.Color(0,0,0);
uint32_t YELLOW_2 = strip.Color(2,2,0);
uint32_t YELLOW_3 = strip.Color(9,9,0);
uint32_t YELLOW_4 = strip.Color(22,22,0);
uint32_t YELLOW_5 = strip.Color(43,43,0);
uint32_t YELLOW_6 = strip.Color(75,75,0);
uint32_t YELLOW_7 = strip.Color(119,119,0);
uint32_t YELLOW_8 = strip.Color(179,179,0);
uint32_t YELLOW_9 = strip.Color(255,255,0);


uint32_t GREEN_0 = strip.Color(0,0,0);
uint32_t GREEN_1 = strip.Color(0,0,0);
uint32_t GREEN_2 = strip.Color(2,0,0);
uint32_t GREEN_3 = strip.Color(9,0,0);
uint32_t GREEN_4 = strip.Color(22,0,0);
uint32_t GREEN_5 = strip.Color(43,0,0);
uint32_t GREEN_6 = strip.Color(75,0,0);
uint32_t GREEN_7 = strip.Color(119,0,0);
uint32_t GREEN_8 = strip.Color(179,0,0);
uint32_t GREEN_9 = strip.Color(255,0,0);


uint32_t TEAL_0 = strip.Color(0,0,0);
uint32_t TEAL_1 = strip.Color(0,0,0);
uint32_t TEAL_2 = strip.Color(2,0,2);
uint32_t TEAL_3 = strip.Color(9,0,9);
uint32_t TEAL_4 = strip.Color(22,0,22);
uint32_t TEAL_5 = strip.Color(43,0,43);
uint32_t TEAL_6 = strip.Color(75,0,75);
uint32_t TEAL_7 = strip.Color(119,0,119);
uint32_t TEAL_8 = strip.Color(179,0,179);
uint32_t TEAL_9 = strip.Color(255,0,255);


uint32_t BLUE_0 = strip.Color(0,0,0);
uint32_t BLUE_1 = strip.Color(0,0,0);
uint32_t BLUE_2 = strip.Color(0,0,2);
uint32_t BLUE_3 = strip.Color(0,0,9);
uint32_t BLUE_4 = strip.Color(0,0,22);
uint32_t BLUE_5 = strip.Color(0,0,43);
uint32_t BLUE_6 = strip.Color(0,0,75);
uint32_t BLUE_7 = strip.Color(0,0,119);
uint32_t BLUE_8 = strip.Color(0,0,179);
uint32_t BLUE_9 = strip.Color(0,0,255);


uint32_t FUCHA_0 = strip.Color(0,0,0);
uint32_t FUCHA_1 = strip.Color(0,0,0);
uint32_t FUCHA_2 = strip.Color(0,2,1);
uint32_t FUCHA_3 = strip.Color(0,9,3);
uint32_t FUCHA_4 = strip.Color(0,22,8);
uint32_t FUCHA_5 = strip.Color(0,43,17);
uint32_t FUCHA_6 = strip.Color(0,75,29);
uint32_t FUCHA_7 = strip.Color(0,119,47);
uint32_t FUCHA_8 = strip.Color(0,179,70);
uint32_t FUCHA_9 = strip.Color(0,255,100);


uint32_t PURPLE_0 = strip.Color(0,0,0);
uint32_t PURPLE_1 = strip.Color(0,0,0);
uint32_t PURPLE_2 = strip.Color(0,1,2);
uint32_t PURPLE_3 = strip.Color(0,6,9);
uint32_t PURPLE_4 = strip.Color(0,14,22);
uint32_t PURPLE_5 = strip.Color(0,29,43);
uint32_t PURPLE_6 = strip.Color(0,50,75);
uint32_t PURPLE_7 = strip.Color(0,79,119);
uint32_t PURPLE_8 = strip.Color(0,119,179);
uint32_t PURPLE_9 = strip.Color(0,170,255);


uint32_t WHITE_0 = strip.Color(0,0,0);
uint32_t WHITE_1 = strip.Color(0,0,0);
uint32_t WHITE_2 = strip.Color(2,2,2);
uint32_t WHITE_3 = strip.Color(9,9,9);
uint32_t WHITE_4 = strip.Color(22,22,22);
uint32_t WHITE_5 = strip.Color(43,43,43);
uint32_t WHITE_6 = strip.Color(75,75,75);
uint32_t WHITE_7 = strip.Color(119,119,119);
uint32_t WHITE_8 = strip.Color(179,179,179);
uint32_t WHITE_9 = strip.Color(255,255,255);


uint32_t WHITE2_0 = strip.Color(0,0,0);
uint32_t WHITE2_1 = strip.Color(0,0,0);
uint32_t WHITE2_2 = strip.Color(2,2,2);
uint32_t WHITE2_3 = strip.Color(9,9,9);
uint32_t WHITE2_4 = strip.Color(22,22,22);
uint32_t WHITE2_5 = strip.Color(43,43,43);
uint32_t WHITE2_6 = strip.Color(75,75,75);
uint32_t WHITE2_7 = strip.Color(119,119,119);
uint32_t WHITE2_8 = strip.Color(179,179,179);
uint32_t WHITE2_9 = strip.Color(255,255,255);


uint32_t picker(int value){
  if (value < 10 ){thisColor = YELLOW_2;}
  if (value == 10) {thisColor = RED_0;}
  if (value == 11) {thisColor = RED_1;}
  if (value == 12) {thisColor = RED_2;}
  if (value == 13) {thisColor = RED_3;}
  if (value == 14) {thisColor = RED_4;}
  if (value == 15) {thisColor = RED_5;}
  if (value == 16) {thisColor = RED_6;}
  if (value == 17) {thisColor = RED_7;}
  if (value == 18) {thisColor = RED_8;}
  if (value == 19) {thisColor = RED_9;}
  if (value == 20) {thisColor = ORANGE_0;}
  if (value == 21) {thisColor = ORANGE_1;}
  if (value == 22) {thisColor = ORANGE_2;}
  if (value == 23) {thisColor = ORANGE_3;}
  if (value == 24) {thisColor = ORANGE_4;}
  if (value == 25) {thisColor = ORANGE_5;}
  if (value == 26) {thisColor = ORANGE_6;}
  if (value == 27) {thisColor = ORANGE_7;}
  if (value == 28) {thisColor = ORANGE_8;}
  if (value == 29) {thisColor = ORANGE_9;}
  if (value == 30) {thisColor = YELLOW_0;}
  if (value == 31) {thisColor = YELLOW_1;}
  if (value == 32) {thisColor = YELLOW_2;}
  if (value == 33) {thisColor = YELLOW_3;}
  if (value == 34) {thisColor = YELLOW_4;}
  if (value == 35) {thisColor = YELLOW_5;}
  if (value == 36) {thisColor = YELLOW_6;}
  if (value == 37) {thisColor = YELLOW_7;}
  if (value == 38) {thisColor = YELLOW_8;}
  if (value == 39) {thisColor = YELLOW_9;}
  if (value == 40) {thisColor = GREEN_0;}
  if (value == 41) {thisColor = GREEN_1;}
  if (value == 42) {thisColor = GREEN_2;}
  if (value == 43) {thisColor = GREEN_3;}
  if (value == 44) {thisColor = GREEN_4;}
  if (value == 45) {thisColor = GREEN_5;}
  if (value == 46) {thisColor = GREEN_6;}
  if (value == 47) {thisColor = GREEN_7;}
  if (value == 48) {thisColor = GREEN_8;}
  if (value == 49) {thisColor = GREEN_9;}
  if (value == 50) {thisColor = TEAL_0;}
  if (value == 51) {thisColor = TEAL_1;}
  if (value == 52) {thisColor = TEAL_2;}
  if (value == 53) {thisColor = TEAL_3;}
  if (value == 54) {thisColor = TEAL_4;}
  if (value == 55) {thisColor = TEAL_5;}
  if (value == 56) {thisColor = TEAL_6;}
  if (value == 57) {thisColor = TEAL_7;}
  if (value == 58) {thisColor = TEAL_8;}
  if (value == 59) {thisColor = TEAL_9;}
  if (value == 60) {thisColor = BLUE_0;}
  if (value == 61) {thisColor = BLUE_1;}
  if (value == 62) {thisColor = BLUE_2;}
  if (value == 63) {thisColor = BLUE_3;}
  if (value == 64) {thisColor = BLUE_4;}
  if (value == 65) {thisColor = BLUE_5;}
  if (value == 66) {thisColor = BLUE_6;}
  if (value == 67) {thisColor = BLUE_7;}
  if (value == 68) {thisColor = BLUE_8;}
  if (value == 69) {thisColor = BLUE_9;}
  if (value == 70) {thisColor = FUCHA_0;}
  if (value == 71) {thisColor = FUCHA_1;}
  if (value == 72) {thisColor = FUCHA_2;}
  if (value == 73) {thisColor = FUCHA_3;}
  if (value == 74) {thisColor = FUCHA_4;}
  if (value == 75) {thisColor = FUCHA_5;}
  if (value == 76) {thisColor = FUCHA_6;}
  if (value == 77) {thisColor = FUCHA_7;}
  if (value == 78) {thisColor = FUCHA_8;}
  if (value == 79) {thisColor = FUCHA_9;}
  if (value == 80) {thisColor = PURPLE_0;}
  if (value == 81) {thisColor = PURPLE_1;}
  if (value == 82) {thisColor = PURPLE_2;}
  if (value == 83) {thisColor = PURPLE_3;}
  if (value == 84) {thisColor = PURPLE_4;}
  if (value == 85) {thisColor = PURPLE_5;}
  if (value == 86) {thisColor = PURPLE_6;}
  if (value == 87) {thisColor = PURPLE_7;}
  if (value == 88) {thisColor = PURPLE_8;}
  if (value == 89) {thisColor = PURPLE_9;}
  if (value == 90) {thisColor = WHITE_0;}
  if (value == 91) {thisColor = WHITE_1;}
  if (value == 92) {thisColor = WHITE_2;}
  if (value == 93) {thisColor = WHITE_3;}
  if (value == 94) {thisColor = WHITE_4;}
  if (value == 95) {thisColor = WHITE_5;}
  if (value == 96) {thisColor = WHITE_6;}
  if (value == 97) {thisColor = WHITE_7;}
  if (value == 98) {thisColor = WHITE_8;}
  if (value == 99) {thisColor = WHITE_9;}
  if (value == 100) {thisColor = WHITE2_0;}
  if (value == 101) {thisColor = WHITE2_1;}
  if (value == 102) {thisColor = WHITE2_2;}
  if (value == 103) {thisColor = WHITE2_3;}
  if (value == 104) {thisColor = WHITE2_4;}
  if (value == 105) {thisColor = WHITE2_5;}
  if (value == 106) {thisColor = WHITE2_6;}
  if (value == 107) {thisColor = WHITE2_7;}
  if (value == 108) {thisColor = WHITE2_8;}
  if (value == 109) {thisColor = WHITE2_9;}
  if (value > 109) {thisColor = WHITE2_9;}
  return thisColor;}


  
/*
uint32_t picker(int value){
  if (value == 0){thisColor = OFF;}
  if (value == 1){thisColor = PURPLE;}
  if (value == 2){thisColor = GREEN;}
  if (value == 3){thisColor = TEAL;}
  if (value == 4){thisColor = RED;}
  if (value == 5){thisColor = YELLOW;}
  if (value == 6){thisColor = FUCHA;}
  if (value == 7){thisColor = BLUE;}
  if (value == 8){thisColor = ORANGE;}
  if (value == 9){thisColor = WHITE;}
  if (value == 10){thisColor = NEW;}
  if (value > 10){thisColor = NEW;}
  return thisColor;
}
*/
