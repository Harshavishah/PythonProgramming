import turtle as t
import random

tim = t.Turtle()
colors = ["red","medium blue","magenta","orange","lime","dark violet"]
directions = [0,90,180,200]

for _ in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))