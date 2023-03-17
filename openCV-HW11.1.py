import cv2

evt = 0 
def mouseClick(event,xpos,ypos,flags_placeholder,parameters_placeholder):
    global pnt1
    global pnt2
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Hello: ', event)
        evt = event
        pnt1 = (xpos,ypos)
    if event == cv2.EVENT_LBUTTONUP:
        print('World: ', event)
        evt = event
        pnt2 = (xpos,ypos)
    if event == cv2.EVENT_RBUTTONUP:
        evt = event

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Winds')
cv2.setMouseCallback('Winds', mouseClick) 

while True:
    ignore, frame = cam.read()

    if evt == 4:
        cv2.rectangle(frame, pnt1, pnt2, (0,0,255), 2)
        frameroi = frame[pnt1[1] : pnt2[1], pnt1[0] : pnt2[0]] # pnt1/2 is a tuple.. 0th place is the x pos and 1th place is the y pos
        cv2.imshow('WINDOS', frameroi)
        cv2.moveWindow('WINDOS', width, 0)
    
    if evt == 5:
        cv2.destroyWindow('WINDOS')
        evt = 0

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()