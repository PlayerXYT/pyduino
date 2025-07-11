#define W_LOW 0
#define W_HIGH 1
#define S_OUT 2
#define S_IN 3
#define S_INP 4
#define READ 5
#define A_READ 6
#define A_WRITE 7

void setup() {
	Serial.begin(9600);
}

void loop() {
	if(Serial.available()) {
		byte in = Serial.read();
		in -= 31;
		byte type = get_type(in);
		while(in>13) in-=13;
		
		switch(type) {
			case W_LOW:
				digitalWrite(in, LOW);
				break;
			case W_HIGH:
				digitalWrite(in, HIGH);
				break;
			case S_OUT:
				pinMode(in, OUTPUT);
				break;
			case S_IN:
				pinMode(in, INPUT);
				break;
			case S_INP:
				pinMode(in, INPUT_PULLUP);
				break;
			case READ:
				Serial.println(digitalRead(in));
				break;
			case A_READ:
				Serial.println(analogRead(in));
				break;
			case A_WRITE:
				analogWrite(in, Serial.read());
		}
	}
}

byte get_type(byte data) {
	if(data>91) return A_WRITE;
	if(data>78) return A_READ;
	if(data>65) return READ;
	if(data>52) return S_INP;
	if(data>39) return S_IN;
	if(data>26) return S_OUT;
	if(data>13) return W_HIGH;
	return W_LOW;
}
