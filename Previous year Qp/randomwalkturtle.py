from turtle import Turtle
import random

def randomwalk(t, turns, distance=20):
    for i in range(turns):
        t.left(random.randint(0, 360))
        t.forward(distance)
t = Turtle()
randomwalk(t, 40)
