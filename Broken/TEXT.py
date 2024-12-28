# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:16:41 2022

@author: mac
"""
a = []
f = open("D:/Python/Broken/test1.txt",'r')
for i in f.readlines():
    if len(i):
        try:
            a.append(float(i.strip()))
        except:
            pass
b = []
for t in range(1,len(a)):
    b.append(a[t]-a[t-1])
xm = sum(b)/len(b)
s = 0
for k in b:
    s += (k-xm)**2
re = s/len(b)
print(re)