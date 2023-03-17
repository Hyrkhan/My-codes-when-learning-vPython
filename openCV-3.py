#this are some improvements for the program
import cv2

width = 320
height = 180

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #capture the frame and do a direct show
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Webcam1', frame)
    cv2.moveWindow('Webcam1',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cam.release()