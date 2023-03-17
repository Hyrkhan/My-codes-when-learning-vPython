import cv2

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

evt = 0 # give it a value first for the global variable to last

#function will take an event(what you did with the mouse, like left click-right click) and the position of the cursor where the mouse event occured
def mouseClick(event,xpos,ypos,flags_placeholder,parameters_placeholder):
    global evt # create a global variable so that you can use it on other codes
    global pnt # create a global variable again for the position of the mouse, make it a tuple
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Hello: ', event)
        print('at position: ',xpos ,ypos)
        pnt = (xpos,ypos)
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        print('World: ', event)
        print('at position: ',xpos ,ypos)
        evt = event
        pnt = (xpos,ypos)
    if event == cv2.EVENT_RBUTTONUP:
        print('Hell: ', event)
        pnt = (xpos,ypos)
        evt = event

cv2.namedWindow('Winds')

cv2.setMouseCallback('Winds', mouseClick) # name of the window, then what function you will run

while True:
    ignore, frame = cam.read()

    if evt == 1 or evt == 4:
        cv2.circle(frame, pnt, 25,(255,0,0),2)

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()
