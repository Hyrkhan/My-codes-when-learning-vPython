import cv2 #import the cv2 library to use its functions
print(cv2.__version__) #double check the version of the cv2

cam = cv2.VideoCapture(0) #make a variable and get the camera you will use. different camera means different index. I only have 1 camera thats why its on 0 index

while True: #basically like an animation, get the frames continously and show it to the screen continously to show a video
    ignore, frame = cam.read() #syntax for getting the frame, read the cam and store it on a variable
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #create a new variable and turn the captured frame by the camera into black n white color using this syntax

    cv2.imshow('my Webcam', grayframe) #syntax for showing the frame captured in the camera, name the webcam window.

    cv2.moveWindow('my Webcam', 10, 10) #move window to a fixed location in the screen
    if cv2.waitKey(1) & 0xff == ord('q'): #syntax for the exit. when I press the 'q' in keyboard, the while loop will stop/break. Waitkey means wait for 1 second.
        break

cam.release() #release the camera that is used