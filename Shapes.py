import turtle as t
import random

tim = t.Turtle()

colors =["red","medium blue","magenta","orange","lime","dark violet"]
def draw_shape(num_sides):

    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_sides_n in range(3,11):
    tim.color(random.choice(colors))
    tim.pensize(2)
    draw_shape(shape_sides_n)