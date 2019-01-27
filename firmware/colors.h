
#define PIN 6
#define leds 22
#define rows 11

Adafruit_NeoPixel strip = Adafruit_NeoPixel(leds*rows, PIN, NEO_RGB + NEO_KHZ800);

uint32_t RED = strip.Color(0,255,0);
uint32_t ORANGE = strip.Color(100,255,0);
uint32_t YELLOW = strip.Color(255,255,0);
uint32_t GREEN = strip.Color(255,0,0);
uint32_t TEAL = strip.Color(255,0,255);
uint32_t BLUE = strip.Color(0,0,255);
uint32_t FUCHA = strip.Color(0,255,100);
uint32_t PURPLE = strip.Color(0,170,255);
uint32_t NEW = strip.Color(170,120,66);
uint32_t WHITE = strip.Color(255,255,255);
uint32_t OFF = strip.Color(0,0,0);

uint32_t RED_0 = strip.Color(0,0,0);
uint32_t RED_1 = strip.Color(0,28,0);
uint32_t RED_2 = strip.Color(0,56,0);
uint32_t RED_3 = strip.Color(0,84,0);
uint32_t RED_4 = strip.Color(0,112,0);
uint32_t RED_5 = strip.Color(0,140,0);
uint32_t RED_6 = strip.Color(0,168,0);
uint32_t RED_7 = strip.Color(0,196,0);
uint32_t RED_8 = strip.Color(0,224,0);
uint32_t RED_9 = strip.Color(0,252,0);


uint32_t ORANGE_0 = strip.Color(0,0,0);
uint32_t ORANGE_1 = strip.Color(11,28,0);
uint32_t ORANGE_2 = strip.Color(22,56,0);
uint32_t ORANGE_3 = strip.Color(33,84,0);
uint32_t ORANGE_4 = strip.Color(44,112,0);
uint32_t ORANGE_5 = strip.Color(55,140,0);
uint32_t ORANGE_6 = strip.Color(66,168,0);
uint32_t ORANGE_7 = strip.Color(77,196,0);
uint32_t ORANGE_8 = strip.Color(88,224,0);
uint32_t ORANGE_9 = strip.Color(99,252,0);


uint32_t YELLOW_0 = strip.Color(0,0,0);
uint32_t YELLOW_1 = strip.Color(28,28,0);
uint32_t YELLOW_2 = strip.Color(56,56,0);
uint32_t YELLOW_3 = strip.Color(84,84,0);
uint32_t YELLOW_4 = strip.Color(112,112,0);
uint32_t YELLOW_5 = strip.Color(140,140,0);
uint32_t YELLOW_6 = strip.Color(168,168,0);
uint32_t YELLOW_7 = strip.Color(196,196,0);
uint32_t YELLOW_8 = strip.Color(224,224,0);
uint32_t YELLOW_9 = strip.Color(252,252,0);


uint32_t TEAL_0 = strip.Color(0,0,0);
uint32_t TEAL_1 = strip.Color(28,0,28);
uint32_t TEAL_2 = strip.Color(56,0,56);
uint32_t TEAL_3 = strip.Color(84,0,84);
uint32_t TEAL_4 = strip.Color(112,0,112);
uint32_t TEAL_5 = strip.Color(140,0,140);
uint32_t TEAL_6 = strip.Color(168,0,168);
uint32_t TEAL_7 = strip.Color(196,0,196);
uint32_t TEAL_8 = strip.Color(224,0,224);
uint32_t TEAL_9 = strip.Color(252,0,252);


uint32_t GREEN_0 = strip.Color(0,0,0);
uint32_t GREEN_1 = strip.Color(28,0,0);
uint32_t GREEN_2 = strip.Color(56,0,0);
uint32_t GREEN_3 = strip.Color(84,0,0);
uint32_t GREEN_4 = strip.Color(112,0,0);
uint32_t GREEN_5 = strip.Color(140,0,0);
uint32_t GREEN_6 = strip.Color(168,0,0);
uint32_t GREEN_7 = strip.Color(196,0,0);
uint32_t GREEN_8 = strip.Color(224,0,0);
uint32_t GREEN_9 = strip.Color(252,0,0);


uint32_t BLUE_0 = strip.Color(0,0,0);
uint32_t BLUE_1 = strip.Color(0,0,28);
uint32_t BLUE_2 = strip.Color(0,0,56);
uint32_t BLUE_3 = strip.Color(0,0,84);
uint32_t BLUE_4 = strip.Color(0,0,112);
uint32_t BLUE_5 = strip.Color(0,0,140);
uint32_t BLUE_6 = strip.Color(0,0,168);
uint32_t BLUE_7 = strip.Color(0,0,196);
uint32_t BLUE_8 = strip.Color(0,0,224);
uint32_t BLUE_9 = strip.Color(0,0,252);


uint32_t FUCHA_0 = strip.Color(0,0,0);
uint32_t FUCHA_1 = strip.Color(0,28,11);
uint32_t FUCHA_2 = strip.Color(0,56,22);
uint32_t FUCHA_3 = strip.Color(0,84,33);
uint32_t FUCHA_4 = strip.Color(0,112,44);
uint32_t FUCHA_5 = strip.Color(0,140,55);
uint32_t FUCHA_6 = strip.Color(0,168,66);
uint32_t FUCHA_7 = strip.Color(0,196,77);
uint32_t FUCHA_8 = strip.Color(0,224,88);
uint32_t FUCHA_9 = strip.Color(0,252,99);


uint32_t PURPLE_0 = strip.Color(0,0,0);
uint32_t PURPLE_1 = strip.Color(0,18,28);
uint32_t PURPLE_2 = strip.Color(0,36,56);
uint32_t PURPLE_3 = strip.Color(0,54,84);
uint32_t PURPLE_4 = strip.Color(0,72,112);
uint32_t PURPLE_5 = strip.Color(0,90,140);
uint32_t PURPLE_6 = strip.Color(0,108,168);
uint32_t PURPLE_7 = strip.Color(0,126,196);
uint32_t PURPLE_8 = strip.Color(0,144,224);
uint32_t PURPLE_9 = strip.Color(0,162,252);


uint32_t WHITE_0 = strip.Color(0,0,0);
uint32_t WHITE_1 = strip.Color(28,28,28);
uint32_t WHITE_2 = strip.Color(56,56,56);
uint32_t WHITE_3 = strip.Color(84,84,84);
uint32_t WHITE_4 = strip.Color(112,112,112);
uint32_t WHITE_5 = strip.Color(140,140,140);
uint32_t WHITE_6 = strip.Color(168,168,168);
uint32_t WHITE_7 = strip.Color(196,196,196);
uint32_t WHITE_8 = strip.Color(224,224,224);
uint32_t WHITE_9 = strip.Color(252,252,252);
