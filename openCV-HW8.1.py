import cv2
import time

width = 640
height = 360

xvalue = (int(width/42))
yvalue = (int(height/12))

myradius = 30
myColor = (0,0,0)
mythickness = 2
myText = 'Hello World'
myFont = cv2.FONT_HERSHEY_DUPLEX

upperleft = (250, 140) 
lowerright = (390, 220)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
tlast = time.time()

fpsFilter = 0

time.sleep(.1)

while True:
    dt = time.time()-tlast
    #fps = 1//dt
    fps = 1/dt
    fpsFilter = fpsFilter * .7 + fps * .3 # filter value using the trust system, calculating using trust needs the two values to equal 1. Put higher value to the one you trust most
    tlast = time.time()

    ignore, frame = cam.read()
    frame[140:220, 250:390 ] = (255,0,0)
    cv2.rectangle(frame, upperleft, lowerright, (0,255,0), 4)
    cv2.circle(frame,(int(width/2),int(height/2)), myradius, myColor, mythickness)
    cv2.putText(frame, myText, (120,60), myFont, 2, (255,0,0), 2) 


    cv2.putText(frame,str(int(fpsFilter)) + ' :fps', (xvalue, yvalue), myFont, .5, (255,255,255), 1)

    cv2.imshow('Window', frame)
    cv2.moveWindow('Window',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()