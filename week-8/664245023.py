import sys
import serial

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer


# เชื่อมต่อบอร์ดและพอร์ตคอมใช้พอร์ตอะไรแก้ให้ถูก
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

        self.btn_on = QPushButton("15")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า15
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า15ไป
        self.btn_on.clicked.connect(lambda: self.send_command("15"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("30")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า30
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า30ไป
        self.btn_on.clicked.connect(lambda: self.send_command("30"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("45")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า45
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า45ไป
        self.btn_on.clicked.connect(lambda: self.send_command("45"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("90")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า90
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า90ไป
        self.btn_on.clicked.connect(lambda: self.send_command("90"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("125")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า125
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า125ไป
        self.btn_on.clicked.connect(lambda: self.send_command("125"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("135")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า135
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า135ไป
        self.btn_on.clicked.connect(lambda: self.send_command("135"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        self.btn_on = QPushButton("150")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่า150
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งค่า150ไป
        self.btn_on.clicked.connect(lambda: self.send_command("150"))
        layout.addWidget(self.btn_on)  # เพิ่มปุ่มเข้า layout

        # --Button ปิด -----
        self.btn_off = QPushButton("STOP")  # ปุ่มแสดงว่าเป็นปุ่มที่ส่งค่าหยุด
        # เมื่อคลิกปุ่มนี้จะเชื่อมต่อไปที่บอร์ดและส่งคำสั่งไปยัง Arduino เพื่อหยุดการทำงาน (เช่นหยุดหมุนมอเตอร์)
        self.btn_off.clicked.connect(lambda: self.send_command("OFF"))
        layout.addWidget(self.btn_off)  # เพิ่มปุ่มเข้า layout

        self.setLayout(layout)  # กำหนด layout หลักให้หน้าต่าง

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
