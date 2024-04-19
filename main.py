import random
import turtle


#settings
turtle.title("День открытых дверей!")
t = turtle.Turtle()
turtle.bgcolor("aqua")
t.showturtle()
t.turtlesize(1)
t.shape("turtle")
t.speed(10)


#colors
colors = (
    'red', 'green', 'blue',
    'yellow', 'violet', 'purple',
    'pink',
    )


#flower
for _ in range(7):
    color = random.choice(colors)

    t.begin_fill()
    t.color(color)
    t.circle(100,90)
    t.circle(50,135)
    t.circle(100,90)
    t.end_fill()
    t.rt(10)


t.color("darkcyan")
t.dot(100)


turtle.mainloop()