import cv2

def mycallback1(value):
    global xpos
    xpos = value
def mycallback2(value):
    global ypos
    ypos = value
def mycallback3(value):
    width = value
    height = int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

width = 1280
height = 720

xpos = 0
ypos = 0

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('mytrackbars')
cv2.moveWindow('mytrackbars', width,0)
cv2.resizeWindow('mytrackbars', 400, 150)
cv2.createTrackbar('xpos', 'mytrackbars', 0, 2000, mycallback1)
cv2.createTrackbar('ypos', 'mytrackbars', 0, 1000, mycallback2)
cv2.createTrackbar('Width', 'mytrackbars', width, 1920, mycallback3)

while True:
    ignore, frame = cam.read()

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds', xpos , ypos)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()