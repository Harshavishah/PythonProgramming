import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
#colors = ["red","medium blue","magenta","orange","lime","dark violet"]
directions = [0,90,180,200]
tim.pensize(10)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color=(r,g,b)
    return random_color
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))