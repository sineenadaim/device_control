#include <ESP32Servo.h>        

Servo myservo;                 
String command;                

void setup() {
  Serial.begin(9600);          
  myservo.attach(32);          
  pinMode(2, OUTPUT);          
}

void loop() {
  if (Serial.available()) {                        
    String command = Serial.readStringUntil('\n'); 
    command.trim();                                

    if (command == "15") {                         
      Serial.println("Servo Motor => 15");       
      myservo.write(15);                          
      digitalWrite(2, HIGH);
      delay(500);
      digitalWrite(2, LOW);                                   
    } 
    else if (command == "30") {                    
      Serial.println("Servo Motor => 30");
      myservo.write(30);                          
      digitalWrite(2, HIGH);
      delay(500);
      digitalWrite(2, LOW);                                   
    } 
    else if (command == "60") {                   
      Serial.println("Servo Motor => 60");
      myservo.write(60);                           
      digitalWrite(2, HIGH);
      delay(500);
      digitalWrite(2, LOW);                                   
    } 
    else if (command == "90") {                    
      Serial.println("Servo Motor => 90");
      myservo.write(90);                           
      digitalWrite(2, HIGH);
      delay(500);
      digitalWrite(2, LOW);                        
    }
    else if (command == "115") {                   
      Serial.println("Servo Motor => 115");
      myservo.write(115);                          
      digitalWrite(2, HIGH);                                  
    }
    else if (command == "135") {                   
      Serial.println("Servo Motor => 135");
      myservo.write(135);                          
      digitalWrite(2, HIGH);                                    
    }
    else if (command == "160") {                  
      Serial.println("Servo Motor => 160");
      myservo.write(160);                          
      treeblinkLED();                                   
    }
    else if (command == "OFF"){                    // ถ้าข้อมูลที่รับมาเป็น "OFF"
      Serial.println("Servo Motor => 0");
      myservo.write(0);                            // หมุน Servo กลับไปที่ 0 องศา
      digitalWrite(2, LOW);                        // ปิด LED
    }
    delay(1000);                                   
  }
}


void treeblinkLED(){                                     // ฟังก์ชันสำหรับทำให้ LED กระพริบช้า
  for(int i = 0; i<4; i++){                        
    digitalWrite(2, HIGH);                         
    delay(3000);                                   
    digitalWrite(2, LOW);                          
    delay(3000);                                   
  }
}
