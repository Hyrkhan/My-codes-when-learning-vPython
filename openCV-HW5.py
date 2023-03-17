#make a checkerboard picture using the previous syntaxes
import cv2
print(cv2.__version__)
import numpy as np

while True:
    frame = np.zeros([200,200, 3], dtype=np.uint8) 

    horizontal1 = 0
    horizontal2 = 25
    for i in range (0, 4, 1):
        vertical1 = 0
        vertical2 = 25
        for j in range (0,4,1):
            frame[horizontal1:horizontal2,vertical1:vertical2] = [255,255,255] 
            vertical1 += 50
            vertical2 += 50
        horizontal1 += 50
        horizontal2 += 50
    
    horizontal1 = 25
    horizontal2 = 50
    for k in range (0, 4, 1):
        vertical1 = 25
        vertical2 = 50
        for n in range (0,4,1):
            frame[horizontal1:horizontal2,vertical1:vertical2] = [255,255,255] 
            vertical1 += 50
            vertical2 += 50
        horizontal1 += 50
        horizontal2 += 50
      
    cv2.imshow('My Window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break