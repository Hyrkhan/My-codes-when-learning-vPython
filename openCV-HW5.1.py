import cv2
import numpy as np

boardsize = int(input('What size of the board? '))
numsquares = int(input('Number of squares? '))
squaresize = int(boardsize/numsquares)  # get the square size of the squares for the loop

darkcolor = (0,0,0) # color variables with tuples for the toggle of colors while looping
lightcolor = (0,0,255)
nowcolor = darkcolor    

while True:
    frame = np.zeros([boardsize,boardsize, 3], dtype=np.uint8)
    for row in range(0,numsquares): # loop through the number of all squares
        if nowcolor == darkcolor:
                nowcolor = lightcolor
        else:
            nowcolor = darkcolor
        for column in range (0,numsquares):
            frame[squaresize*row : squaresize * (row+1), squaresize*column : squaresize * (column+1)] = nowcolor # base the pixel location by the index while looping
            if nowcolor == darkcolor:
                nowcolor = lightcolor
            else:
                nowcolor = darkcolor

    cv2.imshow('My Window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break