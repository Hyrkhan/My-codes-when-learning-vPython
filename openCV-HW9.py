#take the main image(whole frame) to grayscale, then have a little colored box and put it on the center,
# the color moves on the screen and bounce like a ball from left,right,up,down
import cv2

width = 1280
height = 720

frameheight1 = 0
frameheight2 = 100

framewidth1 = 0
framewidth2 = 180

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ignore, frame = cam.read()

    frameroi = frame[ frameheight1 : frameheight2, framewidth1 : framewidth2]

    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameroibgr = cv2.cvtColor(framegray, cv2.COLOR_GRAY2BGR)
    
    frameroibgr[ frameheight1 : frameheight2, framewidth1 : framewidth2] = frameroi

    cv2.imshow('Window', frameroibgr)
    #cv2.moveWindow('Window',0,0)

    if frameheight1 == 0:
        varadd = 20
    elif frameheight2 == height-220:
        varadd = -20

    frameheight1 += varadd
    frameheight2 += varadd

    if framewidth1 == 0:
        varadd2 = 20
    elif framewidth2 == int(width/2):
        varadd2 = -20
            
    framewidth1 += varadd2
    framewidth2 += varadd2
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()

"""
Comments
    #frameroi = frame[130:230, 250:390] # int((height/2)-50) : int((height/2)+50), int((width/2)-70) : int((width/2)+70)
    #frameroi = frame[ int((height/2)-50) : int((height/2)+50), int((width/2)-70) : int((width/2)+70)]

    #frameroibgr[ int((height/2)-50) : int((height/2)+50), int((width/2)-70) : int((width/2)+70)] = frameroi
"""