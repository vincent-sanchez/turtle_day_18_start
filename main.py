from turtle import Turtle
from turtle import Screen
from data import shapes

# Create Turtle Object named tim
tim = Turtle()
tim.shape('turtle')

# Function that moves Turtle object.
def move(sides, color):
    tim.color(color)
    angle = 360/sides
    for x in range(sides):
        tim.forward(100)
        tim.right(angle)

# For each shape in the data python list, call move() function
# passing the sides and color values.
for shape in shapes:
    move(shapes[shape]['sides'],shapes[shape]['color'])

screen = Screen()
screen.exitonclick()
