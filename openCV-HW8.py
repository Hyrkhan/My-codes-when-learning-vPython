# calculate on the loop your frames per second, display the txt on upperleft (like 23 fps), this will be like a fps tracker of a game
# everysecond, your computer renders the frames, do some math to get the frames per second on the while loop
import cv2
import time

width = 1280
height = 720

#upperleft = (20,20)
#lowerright = (140,80)  
upperleft = (int(width/64), int(height/32))
lowerright = (int(width/9), int(height/9))

#xvalue = 30 #(int(width/42))
#yvalue = 60 #(int(height/12))
xvalue = (int(width/42))
yvalue = (int(height/12))

myText = ' :fps'
myFont = cv2.FONT_HERSHEY_DUPLEX
fontsize = 0.5

fps = 0
fps2 = 0
start_time = time.perf_counter() # 0 seconds

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:  
    ignore, frame = cam.read()
    current_time = time.perf_counter() # new time variable

    if current_time - start_time >= 1:  # if current time is larger than the starting time
        fps2 = fps
        fps = 0
        start_time = current_time   # restart time value
    else:
        fps += 1

    framespersecond = str(fps2)
    cv2.putText(frame,framespersecond + myText, (xvalue, yvalue), myFont, fontsize, (255,255,255), 1)
    cv2.rectangle(frame, upperleft, lowerright, (0,255,0), 2)

    cv2.imshow('Window', frame)
    cv2.moveWindow('Window',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

cam.release()