#just see how many little windows can this computer run to fill the screen. Observe how many ROWS and how many COLUMNS by using grayframes,windows size manipulation
import cv2

width = 160
height = 90

WebcamString = 'Webcam'

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    xPoint = 0
    for i in range (0,12,1):
            stringUse = WebcamString + str(i)
            cv2.imshow(stringUse, frame)
            cv2.moveWindow(stringUse,xPoint,0)
            xPoint += 160
    xPoint = 0
    for j in range (12,24,1):
            stringUse2 = WebcamString + str(j)
            cv2.imshow(stringUse2, grayframe)
            cv2.moveWindow(stringUse2,xPoint,150)
            xPoint += 160
    xPoint = 0
    for k in range (24,36,1):
            stringUse3 = WebcamString + str(k)
            cv2.imshow(stringUse3, frame)
            cv2.moveWindow(stringUse3,xPoint,300)
            xPoint += 160
    xPoint = 0
    for l in range (36,48,1):
            stringUse4 = WebcamString + str(l)
            cv2.imshow(stringUse4, grayframe)
            cv2.moveWindow(stringUse4,xPoint,450)
            xPoint += 160
    xPoint = 0
    for n in range (48,60,1):
            stringUse5 = WebcamString + str(n)
            cv2.imshow(stringUse5, frame)
            cv2.moveWindow(stringUse5,xPoint,600)
            xPoint += 160
    xPoint = 0
    for m in range (60,72,1):
            stringUse6 = WebcamString + str(m)
            cv2.imshow(stringUse6, grayframe)
            cv2.moveWindow(stringUse6,xPoint,750)
            xPoint += 160
    xPoint = 0
    for o in range (72,84,1):
            stringUse7 = WebcamString + str(o)
            cv2.imshow(stringUse7, frame)
            cv2.moveWindow(stringUse7,xPoint,900)
            xPoint += 160

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cam.release()