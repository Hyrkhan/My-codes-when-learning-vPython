import cv2
import numpy as np

width = 640
height = 360

evt = 0
xposition = 0
yposition = 0

def mouseClick(event, xPos , yPos, flags, params):
    global evt
    global xposition
    global yposition
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xposition = xPos
        yposition = yPos
        evt = event
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        evt = event
        
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myWebcam') # create a windows first before using it on other codes
cv2.setMouseCallback('myWebcam', mouseClick) #to see if theres a click to a window

while True:
    ignore, frame = cam.read()

    if evt == 1:
        x = np.zeros([250, 250, 3], dtype=np.uint8) #250 rows 250 colums 3 colors(RGB)
        y = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert to HSV and grab it
        color = y[yposition][xposition]
        x[:,:] = color
        cv2.putText(x, str(color), (0,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
        cv2.imshow('Color picker', x)
        cv2.moveWindow('Color picker', width, 0)
        evt = 0
        

    cv2.imshow('myWebcam', frame)
    cv2.moveWindow('myWebcam', 0 , 0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()