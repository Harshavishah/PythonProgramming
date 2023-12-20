from turtle import Turtle, Screen

timmy_the_turtle= Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("blue")
timmy_the_turtle.shapesize(0.5)

#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()

