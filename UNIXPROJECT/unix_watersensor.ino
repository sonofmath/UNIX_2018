//www.elegoo.com
//2016.12.9

int adc_id = 0;
int ledPin = 13;
char printBuffer[128];
bool blinkLight = false;
int readInByte = 0;
int counter = 0;

char readBuffer[1];

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  int value = analogRead(adc_id); // get adc value

  sprintf(printBuffer,"%d\n", value);
  Serial.print(printBuffer);
  //digitalWrite(ledPin, HIGH);
  delay(1000);
  //digitalWrite(ledPin, LOW);
  //delay(1000);
  
  if(Serial.available() > 0)
  {
    readBuffer[0] = Serial.read();
    readInByte = atoi(readBuffer);
    if(readInByte == 1)
    {
      while(value < 350)
      {
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        //Serial.print(printBuffer);
        value = analogRead(adc_id);
        sprintf(printBuffer,"%d\n", value);
        Serial.print(printBuffer);
      }
     }
    //sprintf(readBuffer, "%d\n", readInByte);
    //Serial.print(readBuffer);
    Serial.read();
  }
}
