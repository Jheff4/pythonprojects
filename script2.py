import turtle
wn = turtle.Screen()
wn.bgcolor("grey")

alex =turtle.Turtle()
alex.pencolor("blue")
alex.shape("circle")

dist = 5
alex.up()
for _ in range(40):
    alex.stamp()
    alex.forward(dist)
    alex.right(24)
    dist += 3

wn.exitonclick()
