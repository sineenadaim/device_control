import face_recognition
import cv2
import serial
import time
import numpy as np



# โหลดภาพตัวอย่างเจ้าของ (ผู้อนุญาต)
owner_image = face_recognition.load_image_file("user.jpg")
owner_encoding = face_recognition.face_encodings(owner_image)[0]

# เปิดกล้อง
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    # แปลง BGR → RGB และบังคับ dtype เป็น uint8
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame = np.array(rgb_frame, dtype=np.uint8)

    # หาตำแหน่งใบหน้า
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([owner_encoding], face_encoding)

        
    # แสดงภาพจากกล้อง
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()