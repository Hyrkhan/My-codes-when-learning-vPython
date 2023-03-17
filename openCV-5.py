import cv2
print(cv2.__version__)
import numpy as np
while True:
    """
    This is a simple white n black box
    frame = np.zeros([250,250], dtype=np.uint8)
    #frame[:,:] = 255 # all white frame
    #frame[:,:125] = 255 # half white half black frame
    frame[:125,:] = 255 # vertical half white half black frame
    """
    frame = np.zeros([250,250, 3], dtype=np.uint8) # create a tuple (#,#,#) so that colors can be entered in the box (Blue,Green,Red)
    frame[:,:] = [0,0,255] # this makes a red box 
    frame[:,125:] = [0,255,0]
    cv2.imshow('My Window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break