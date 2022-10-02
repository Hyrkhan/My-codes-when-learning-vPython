#1st assignment
#create a 3d room, with floor, ceiling, left/right/and back wall - 10 wide 10 high 10 deep - wall is 10th of an inch thick
#put a marble inside the room 
from vpython import *

floor = box(pos = vector(0,-5,0),color = color.white, length = 10, width = 10, height = .1) #pos = vector (x(left-right),y(up-down),z(forward-backwards)) 
ceiling = box(pos = vector(0,5,0),color = color.white, length = 10, width = 10, height = .1) #length = how long it is in x axis
leftWall = box(pos = vector(-5,0,0),color = color.white, length = .1, width = 10, height = 10) # width = how long it is in z axis
righttWall = box(pos = vector(5,0,0),color = color.white, length = .1, width = 10, height = 10) # hieght = how long it is in y axis
backWall = box(pos = vector(0,0,-5),color = color.white, length = 10, width = .1, height = 10)
marble = sphere(pos = vector(0,-4,0),color = color.yellow, radius = 1)
while True:
    pass