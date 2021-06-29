from turtle import *

shape("turtle")
speed(0)

# forward(100)
# left(45)
# forward(100)
# right(90)
# forward(100)
# backward(200)

def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return 

    forward(size)

    right(angle)
    tree(size*0.8, levels-1, angle)
    
    left(angle*2)
    tree(size*0.8, levels-1, angle)

    right(angle)
    backward(size)

def snowFlakeSide(length, levels):
    if(levels== 0):
        forward(length)
        return

    length/=3.0
    snowFlakeSide(length, levels-1)
    left(60)
    snowFlakeSide(length, levels-1)
    right(120)
    snowFlakeSide(length, levels-1)
    left(60)
    snowFlakeSide(length, levels-1)


def createSnowFlake(sides, length):
    colors=['green',  'red','blue', 'purple',]
    for i in range(sides): 
        color(colors[i])
        snowFlakeSide(length, sides)
        right(360/sides)   

# snowFlakeSide(200, 4)
createSnowFlake(3, 200)

left(90)
tree(70, 5, 30)

mainloop()