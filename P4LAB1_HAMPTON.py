## P4LAB1
## 03/19/2025
## Stephanie Hampton
## Loops and Shapes using Turtle Graphics

# import turtle/window/assign turtle variable
import turtle
win = turtle.Screen()
win.bgcolor('light steel blue')
t = turtle

# way turtle draws
t.pensize(10)
t.color("medium orchid")
t.shape('arrow')

# for loop that runs 4 times
# use range to tell it how many times to run
# range is up to and not inclusive

for square in range(4):
    t.forward(150)
    t.right(90)

#for roof in range(3):
t.left(60)
t.forward(100)
t.right(60)
t.forward(50)
t.right(60)
t.forward(100)

## move away

t.penup()
t.left(180)
t.forward(300)
t.left(20)
t.pendown()

# While loop that runs 3 times
this_run = 0

while this_run < 3:
    t.forward(150)
    t.left(120)
    this_run += 1


#move test
##t.forward(150)
##t.right(90)
##t.forward(600)

# keeps window open after drawing
win.mainloop()


