#create 4 windows colored, b/w, colored, b/w with cv2 

import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Webcam1', frame)
    cv2.moveWindow('Webcam1',0,0)

    cv2.imshow('Webcam2', grayframe)
    cv2.moveWindow('Webcam2', 640, 0)

    cv2.imshow('Webcam3', grayframe)
    cv2.moveWindow('Webcam3', 0, 500)

    cv2.imshow('Webcam4', frame)
    cv2.moveWindow('Webcam4', 640, 500)
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cam.release()