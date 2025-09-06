import sys
import serial

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer



try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
except Exception as e:
    arduino = None
    print("เชื่อมต่อมไม่ได้ :", e)

# สร้างGUI


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino Control")  # ชื่อโปรแกรม
        self.setGeometry(800, 800, 500, 300)  # ขนาด

        layout = QVBoxLayout()
        # --Button เปิด -----

        self.btn_on = QPushButton("15")  
        
        self.btn_on.clicked.connect(lambda: self.send_command("15"))
        layout.addWidget(self.btn_on)  

        self.btn_on = QPushButton("30")  
        
        self.btn_on.clicked.connect(lambda: self.send_command("30"))
        layout.addWidget(self.btn_on) 

        self.btn_on = QPushButton("60")  
        
        self.btn_on.clicked.connect(lambda: self.send_command("60"))
        layout.addWidget(self.btn_on)  
        
        self.btn_on = QPushButton("90") 
        
        self.btn_on.clicked.connect(lambda: self.send_command("90"))
        layout.addWidget(self.btn_on) 

        self.btn_on = QPushButton("115")  
       
        self.btn_on.clicked.connect(lambda: self.send_command("115"))
        layout.addWidget(self.btn_on)  

        self.btn_on = QPushButton("135")  
        
        self.btn_on.clicked.connect(lambda: self.send_command("135"))
        layout.addWidget(self.btn_on) 

        self.btn_on = QPushButton("160") 
       
        self.btn_on.clicked.connect(lambda: self.send_command("160"))
        layout.addWidget(self.btn_on)

        # --Button ปิด -----
        self.btn_off = QPushButton("STOP")  
        
        self.btn_off.clicked.connect(lambda: self.send_command("OFF"))
        layout.addWidget(self.btn_off) 

        self.setLayout(layout)  

    # ฟังก์ชันส่งคำสั่งไปยัง Arduino
    def send_command(self, command):
        if (arduino):
            # แปลง string เป็น byte แล้วส่งไปทาง serial
            arduino.write((command + '\n').encode())
        else:
            QMessageBox.critical(self, "Error", "ไม่พบการเชื่อมต่อ Arduino")


# การสร้าง GUI OUTPUT
# เริ่มต้นโปรแกรมและแสดงหน้าต่าง GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
