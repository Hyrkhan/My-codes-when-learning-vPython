#create a trackbar where it define how big your image(frame) is.
#need to use 16:9 ratio 
#another trackbar to move the frame window (4 directions)

import cv2

def mycallback1(value):
    global xpos
    xpos = value
def mycallback2(value):
    global ypos
    ypos = value
def mycallback3(value):
    global framesize
    framesize = value

width = 1280
height = 720
framesize = 3

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

xpos = width//2
ypos = height//2

cv2.namedWindow('mytrackbars')
cv2.resizeWindow('mytrackbars', 400, 150)
cv2.moveWindow('mytrackbars', width,0)
cv2.createTrackbar('xpos', 'mytrackbars', xpos, 1500, mycallback1)
cv2.createTrackbar('ypos', 'mytrackbars',  ypos, 800, mycallback2)
cv2.createTrackbar('framesize', 'mytrackbars', framesize, 4, mycallback3)

while True:
    ignore, frame = cam.read()

    if framesize == 0:
        width = 80
        height = 45
    elif framesize == 1:
        width = 160
        height = 90
    elif framesize == 2:
        width = 320
        height = 180
    elif framesize == 3:
        width = 640
        height = 360
    elif framesize == 4:
        width = 1280
        height = 720

    frame = cv2.resize(frame, (width, height))

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds', xpos , ypos)

    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()