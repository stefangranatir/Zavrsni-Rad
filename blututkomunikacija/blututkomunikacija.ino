#include <SoftwareSerial.h>

SoftwareSerial serial_connection(2,3);
#define BUFFER_SIZE 64
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i=0;
String inputS;
void setup()
{
  Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("Ready!!!");
  Serial.println("Started");
}
void loop()
{
  
  byte byte_count=serial_connection.available();
  if(byte_count)
  {
    Serial.println("Incoming Data");
    int first_bytes=byte_count; 
    int remaining_bytes=0;
    if(first_bytes>=BUFFER_SIZE-1)
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);
    }
    for(i=0;i<first_bytes;i++)
    {
      inChar=serial_connection.read();
      inData[i]=inChar;
    }
    inData[i]='\0';
   
    inputS=inData;
    int indexZ=inputS.indexOf(',');
    String x=inputS.substring(0,indexZ);
    String y=inputS.substring(indexZ+1, inputS.length());
    Serial.print(inputS);
    Serial.print(x);
    Serial.println(y);

    //debug
    serial_connection.print("X=");
    serial_connection.print(x);
    serial_connection.print(" Y=");
    serial_connection.print(y);
    serial_connection.print(" count= ");
    serial_connection.println(count);
    count++;
  }
  delay(100);
}
