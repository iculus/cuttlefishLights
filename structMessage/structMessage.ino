int incomingByte = 0;    // for incoming serial data

void setup() {
    Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
}


struct Message1 {
  uint8_t a;
  uint8_t b;
  uint8_t c;
  uint8_t d;
} __packed__;
static const size_t MSG_LEN = sizeof(struct Message1);

void loop() {
  //Serial.println("here");
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
        Serial.print(msg1.a, DEC);
        Serial.print(msg1.b, DEC);
        Serial.print(msg1.c, DEC);
        Serial.println(msg1.d, DEC);
        num_payload_chars = MSG_LEN + 1;
      } else {
        num_payload_chars = MSG_LEN + 1;  // invalid packet, drop data
      }
    } else {
      //assert(false);
    }    
  }
  
}
