#create a region of interest using your mouse. when press the left button, that corner will be the region of interest and when you drag it, then you lift the left up, that will be the other corner
# first click is the upper left, the let it up will be the lower right
# that region of interest will show up as a different window
# then if you right mouse click, it will kill the region of interest window
import cv2

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

evt = 0 
upperleft = (0,0)
lowerright = (0,0)

xposition1 = 0
yposition1 = 0
xposition2 = 0
yposition2 = 0

def mouseClick(event,xpos,ypos,flags_placeholder,parameters_placeholder):
    global evt 
    global upperleft
    global lowerright
    global xposition1
    global yposition1
    global xposition2
    global yposition2
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Hello: ', event)
        print('at position: ',xpos ,ypos)
        evt = event
        upperleft = (xpos,ypos)
        xposition1 = xpos
        yposition1 = ypos
    if event == cv2.EVENT_LBUTTONUP:
        print('World: ', event)
        print('at position: ',xpos ,ypos)
        evt = event
        lowerright = (xpos,ypos)
        xposition2 = xpos
        yposition2 = ypos
    if event == cv2.EVENT_RBUTTONUP:
        evt = event

cv2.namedWindow('Winds')
cv2.setMouseCallback('Winds', mouseClick) 

while True:
    ignore, frame = cam.read()

    if evt == 4:
        cv2.rectangle(frame, upperleft, lowerright, (0,255,0), 2)
        frameroi = frame[yposition1:yposition2, xposition1:xposition2]
        cv2.imshow('WINDOS', frameroi)
        cv2.moveWindow('WINDOS', width, 0)
    
    if evt == 5:
        cv2.destroyAllWindows
        break

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()