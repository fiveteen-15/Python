# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:23:06 2023

@author: HUAWEI2
"""

import turtle
from matplotlib import pyplot as plt
from random import randint

x = [] ; y = []
po = [0,0]
act = [-1,1]
pen = turtle.Pen()
pen.pen(speed = 0)

x.append(po[0])
y.append(po[1])

for i in range(1000):
    t = randint(0,3)
    angle = 90*(t+1)+90
    po[t%2] += act[t//2]
    x.append(po[0])
    y.append(po[1])
    pen.left(angle)
    pen.forward(10)
    pen.right(angle)
    print(i+1)
    
plt.scatter(x,y)
plt.show()