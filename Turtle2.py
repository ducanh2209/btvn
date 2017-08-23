from turtle import *

for n in range(6,2,-1):
    if n == 5 or n == 3:
        color("blue")
    else:
        color("red")
    for i in range(n):
        forward(100)
        left(360/n)