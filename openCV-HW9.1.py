#this program uses the middle of a box and move it. the logic will be about that circle
import cv2

width = 640
height = 360

snipW = 120
snipH = 60

boxCenterRow = height // 2
boxCenterColumn = width // 2

deltaRow = 10
deltaColumn = 10

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ignore, frame = cam.read()

    frameroi = frame[int(boxCenterRow-snipH/2) : int(boxCenterRow+snipH/2), int(boxCenterColumn-snipW/2) : int(boxCenterColumn+snipW/2)]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCenterRow-snipH/2) : int(boxCenterRow+snipH/2), int(boxCenterColumn-snipW/2) : int(boxCenterColumn+snipW/2)] = frameroi

    if boxCenterRow-snipH/2 <= 0 or boxCenterRow+snipH/2 >= height:
        deltaRow = deltaRow * (-1)
    if boxCenterColumn-snipW/2 <= 0 or boxCenterColumn+snipW/2 >= width:
        deltaColumn = deltaColumn * (-1)

    boxCenterRow = boxCenterRow + deltaRow
    boxCenterColumn = boxCenterColumn + deltaColumn

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds',0,0)
    cv2.imshow('Window', frameroi)
    cv2.moveWindow('Window',width,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()
