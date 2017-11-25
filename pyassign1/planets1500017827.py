"""Solar System.py: Description of the Solar System.

__author__ = "Zhou Xu-yuan"
__pkuid__  = "1500017827"
__email__  = "1500017827@pku.edu.cn"
"""

import math as mt
import turtle


def main():
    """main module
    """


wn = turtle.Screen()
wn.bgcolor(50, 10, 250)

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()
P = [a, b, c, d, e, f, g, h]
s = turtle.Turtle()

s.shape("circle")
s.color(250, 30, 10)
s.up()
s.goto(80, 0)
s.down()
for i in range(8):
    P[i].speed(0)
    P[i].shape("circle")
    P[i].color((50+60*i) % 255, (120+70*i) % 240, (200+25*i) % 255)
    P[i].up()
    P[i].goto((187-17*i)*mt.cos(mt.pi*10*i**2/180)+4*i, (165-15*i)*mt.sin(mt.pi*10*i**2/180))
    P[i].down()

for n in range(3601):
    for i in range(8):
        r = P[i].distance(80, 0)
        P[i].speed((540+30*i)**2/r**2)
        P[i].goto((187-17*i)*mt.cos(mt.pi*(4.5/(11-i)**0.5*n+10*i**2)/180)+4*i,
                  (165-15*i)*mt.sin(mt.pi*(4.5/(11-i)**0.5*n+10*i**2)/180))


if __name__ == '__main__':
    main()
