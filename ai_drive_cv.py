import cv2
import numpy as np
import requests
url="http://IP_over_LAN/shot.jpg"
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand_detection_weights.xml')

count = 0
  
""" AI-CV Driven vehicle
If the Driver wants to start the car , place both the hands on the steering wheel (forward) .
If the Driver is having no hands on the steering wheel, brakes of the car will be applied slowly.
If one hand is detected on the steering wheel, the Driver can drive upto a certain limit due to safety purpose.
If the Driver is having both of his hands on the steering wheel, the Driver can drive at any any speed ( upto the max limit of car ) .
"""

while True:
    ret, frame = cap.read()
    #frame=requests.get(url)
    #frame=np.array(bytearray(frame.content),dtype=np.uint8)
    #frame=cv2.imdecode(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)
  
    if count==0:
  
        if len(contour)==2:
            cv2.putText(img=frame, text='Your Engine has started',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale=1, color=(0, 255, 0))
                          
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1
  
    if count>0:
  
        if len(contour)>=2:
            cv2.putText(img=frame, text='You can Drive',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale=1, color=(255, 0, 0))
                          
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
              
  
        elif len(contour)==1:
            cv2.putText(img=frame, text='You can speed upto max 80km/h',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale=1, color=(0, 255, 0))
                          
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
        elif len(contour)==0:
            cv2.putText(img=frame, text='Breaks being applied',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale=1, color=(0, 0, 255))
  
        count += 1
  
    cv2.imshow('Driver_Frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc Key
        break