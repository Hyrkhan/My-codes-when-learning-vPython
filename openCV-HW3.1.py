#tutorial solution to the homework
import cv2

rows = int(input('Enter how many Rows: '))
columns = int(input('Enter how many Columns: '))

width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/columns))) # x and y size needs to be inside a parenthesis

    for i in range (0, rows):
        for j in range(0, columns):
            windowname = 'Window' +str(i)+ 'x' +str(j)
            cv2.imshow(windowname,frame)
            cv2.moveWindow(windowname, int(width/columns) * j , int(height/columns + 30) * i)  # 30pixels is the window frame size

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cam.release()