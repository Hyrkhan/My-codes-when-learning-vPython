#create two windows
#1st window left to right will change hue 0 - 179, up to down will change saturation from 0 - 255 and all of value is 255
#2nd windows left to right will change hue 0 - 179, up to down will change value from 0 - 255 and all saturation is 255

import cv2
import numpy as np

x = np.zeros([256,720,3],dtype=np.uint8) # empty box window
for row in range(0, 256, 1): #up to down
    for column in range(0, 720, 1): #left to right
        x[row,column] = (column//4,row,255) #this is a hsv, column is hue and row is saturation. it will iterate all the hues depending on the saturation every loop
x = cv2.cvtColor(x,cv2.COLOR_HSV2BGR) #convert the hsv box first to bgr so that the window will show on the screen

y = np.zeros([256,720,3],dtype=np.uint8) # another empty box for the next window
for row in range(0, 256, 1):
    for column in range(0, 720, 1):
        y[row,column] = (column//4,255,row) # this time, the saturation is fixed at maximum while the value changes from max to black
y = cv2.cvtColor(y,cv2.COLOR_HSV2BGR) 

while True:
    cv2.imshow("my HSV 1", x)
    cv2.moveWindow("my HSV 1", 0, 0)

    cv2.imshow("my HSV 2", y)
    cv2.moveWindow("my HSV 2", 0, row+35)
    
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cv2.destroyAllWindows

"""
When the code "x[row,column] = (column//4,row,255)" is written, the x window is either a bgr or hsv image.
Unless you used a function that will tell it otherwise, it is by default a bgr image.
But since I used the hsv2bgr function, it became an hsv that is converted to bgr instead
"""