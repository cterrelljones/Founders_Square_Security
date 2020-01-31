import numpy as np
import cv2
import random
import time 
import keyboard

face_cascade = cv2.CascadeClassifier('face_detection_project/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

rand = time.time()

while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x,y,w,h) in faces:
        print('I found your face')
        roi_gray = gray[y:y+h, x:x+w]
        for i in range(5):
            img_item = f"face_app/static/temp_img/img{i}.png"
            cv2.imwrite(img_item, roi_gray)
            time.sleep(3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
    if keyboard.is_pressed('q'):
        cap.release()
        cv2.destroyAllWindows()
