
#include "MeOrion.h"

MeDCMotor motor1(M1);

MeDCMotor motor2(M2);

MeUltrasonicSensor ultraSensor(PORT_3); /* Ultrasonic module can ONLY be connected to port 3, 4, 6, 7, 8 of base shield. */

void setup()
{
  motor1.run(-255);
  motor2.run(-255);
}

void loop()
{
  int dist = ultraSensor.distanceCm();
  if(dist<=40 && dist>20){
    motor1.run(-110);
    motor2.run(-110);
  }
  else if(dist<=20 && dist>6){
      motor1.run(-50);
      motor2.run(-50);
      
    }
 else if(dist<=6){
      motor1.run(0);
      motor2.run(0);
      
    }
  Serial.print("Distance : ");
  Serial.print(ultraSensor.distanceCm() );
  Serial.println(" cm");
  delay(10); /* the minimal measure interval is 100 milliseconds */
}

