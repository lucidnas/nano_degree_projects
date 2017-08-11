import turtle

def loop(object, tangle, bangle):
    for i in range(2):
        object.left(tangle)
        object.forward(100)
        for i in range(1):
            object.left(bangle)
            object.forward(100)

    object.left(5)

def draw_object():
    window = turtle.Screen()
    window.bgcolor("white")

    triangle = turtle.Turtle()
    triangle.speed(20)

    triangle.color("blue", "yellow")
    triangle.turtlesize(5)
    for i in range(80):
        loop(triangle, 120, 60)

    triangle.right(130)
    triangle.forward(300)

    window.exitonclick()

draw_object()


