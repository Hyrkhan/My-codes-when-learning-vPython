#1st assignment
#create a 3d room, with floor, ceiling, left/right/and back wall - 10 wide 10 high 10 deep - wall is 10th of an inch thick
#put a marble inside the room 
from vpython import *
from time import *

mRadius = .75
wallThick = .1 
roomWidth = 10 # x 
roomHeight = 10 # y
roomDepth = 10  # z


#floor = box(pos = vector(0,-5,0),color = color.white, length = 10, width = 10, height = .1) #pos = vector (x(left-right),y(up-down),z(forward-backwards)) 
floor = box(pos = vector(0,-roomHeight/2 ,0),color = color.white, size = vector(roomWidth, wallThick, roomDepth)) #size = vector (x,y,z) is the same as length,width,height

#ceiling = box(pos = vector(0,5,0),color = color.white, length = 10, width = 10, height = .1) #length = how long it is in x axis
ceiling = box(pos = vector(0,roomHeight/2 ,0),color = color.white, size = vector(roomWidth, wallThick, roomDepth))

#backWall = box(pos = vector(0,0,-5),color = color.white, length = 10, width = .1, height = 10)
backWall = box(pos = vector(0,0,-roomDepth/2),color = color.white, size = vector(roomWidth, roomHeight, wallThick))

#leftWall = box(pos = vector(-5,0,0),color = color.white, length = .1, width = 10, height = 10) # width = how long it is in z axis
leftWall = box(pos = vector(-roomWidth/2 ,0,0),color = color.white, size = vector(wallThick, roomHeight, roomDepth))

#righttWall = box(pos = vector(5,0,0),color = color.white, length = .1, width = 10, height = 10) # hieght = how long it is in y axis
righttWall = box(pos = vector(roomWidth/2 ,0,0),color = color.white, size = vector(wallThick, roomHeight, roomDepth))

marble = sphere(pos = vector(0,0,0),color = color.yellow, radius = mRadius)

deltax = .1 #a variable that stores a small value
xPos = 0    # a variable to be used

while True:
    rate(30) # how fast the animation goes
    xPos = xPos + deltax    # every rate refresh, the value adds up
    if xPos > roomWidth/2 or xPos < -roomWidth/2:   # if the ball reaches the rightWall or the leftWall
        deltax = deltax * (-1)  # decrease the deltax 
    marble.pos = vector(xPos, 0, 0)   #update the vector position of the marble so that it will change position every rate refresh, hence the animation illusion