import cv2

width = 640
height = 360

myradius = 30
myColor = (0,0,0)
mythickness = 2
myText = 'Hello World'
myFont = cv2.FONT_HERSHEY_DUPLEX

upperleft = (250, 140) #(int((width/4)-40),int((height/4)=40))
lowerright = (390, 220) # (int((width/4)+40), int((height/4)+40)))

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame[140:220, 250:390 ] = (255,0,0)
    cv2.rectangle(frame, upperleft, lowerright, (0,255,0), 4) # (frame, (x, y), (x, y), (color), size) # x axis first then y axis
    # cv2.circle(frame,(320,180), 25, (0,0,0), 2) # (frame, (x, y),(radius), (color), size)
    cv2.circle(frame,(int(width/2),int(height/2)), myradius, myColor, mythickness)
    cv2.putText(frame, myText, (120,60), myFont, 2, (255,0,0), 2) # (frame, text, (x,y), font, fontsize, fontcolor, fontweight)


    cv2.imshow('Window', frame)
    cv2.moveWindow('Window',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()