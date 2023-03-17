import cv2

width = 640
height = 360


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    ignore, frame = cam.read()
    frameroi = frame[150:210, 250:390] 
    frameroigray = cv2.cvtColor(frameroi, cv2.COLOR_BGR2GRAY)
   
    framebgr = cv2.cvtColor(frameroigray, cv2.COLOR_GRAY2BGR)

    frame[150:210, 250:390] = framebgr

    cv2.imshow('Window', frame)
    cv2.moveWindow('Window',0,0)

    cv2.imshow('Window3', frameroigray)
    cv2.moveWindow('Window3',650,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()