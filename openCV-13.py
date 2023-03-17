import cv2

def mycallback1(value):
    global xpos
    print("xpos = " ,value)
    xpos = value
def mycallback2(value):
    global ypos
    print("ypos = ",value)
    ypos = value
def mycallback3(value):
    global myrad
    print("radius = ", value)
    myrad = value
def mycallback4(value):
    global thickness
    print("thickness = ", value)
    thickness = value

width = 1280
height = 720
myrad = 25
thickness = 2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

xpos = width//2
ypos = height//2

cv2.namedWindow('mytrackbars')
cv2.resizeWindow('mytrackbars', 400, 150)
cv2.moveWindow('mytrackbars', width,0)
cv2.createTrackbar('xpos', 'mytrackbars', xpos, width, mycallback1)
cv2.createTrackbar('ypos', 'mytrackbars',  ypos, height, mycallback2)
cv2.createTrackbar('radius', 'mytrackbars', myrad, height//2, mycallback3)
cv2.createTrackbar('thickness', 'mytrackbars', thickness, 25, mycallback4)

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    if thickness == 0:
        thickness = (-1)

    cv2.circle(frame , (xpos,ypos), myrad, (255,0,0), thickness)

    cv2.imshow('Winds', frame)
    cv2.moveWindow('Winds', 0 , 0)

    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()