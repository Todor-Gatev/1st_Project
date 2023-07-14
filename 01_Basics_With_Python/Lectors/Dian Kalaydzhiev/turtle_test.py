import turtle
from turtle import *

color('red', 'yellow')
turtle.speed(7000)
begin_fill()
while True:
    # forward(200)
    # left(170)

    forward(290)
    left(170)

    # forward(290)
    # left(120)
    # right(23)
    if abs(pos()) < 1:
        break
end_fill()
done()
