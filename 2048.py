 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import *

def move_w():
    num=0
    for j in range(1,9,2):
        a0=""
        pos1=0
        for i in range(4):
            if a[i][j]!="    ":
                if a0 != a[i][j]:
                    a0=a[i][j]
                    a[pos1][j],a[i][j]=a[i][j],a[pos1][j]
                    pos1+=1
                else:
                    a[pos1-1][j]=str(int(a[pos1-1][j])*2)+(4-len(str(int(a[pos1-1][j])*2)))*" "
                    a[i][j]="    "
                    a0=a[pos1-1][j]
                    num+=1
            else:
                num+=1
    return num
def move_s():
    num=0
    for j in range(1,9,2):
        a0=""
        pos1=-1
        for i in range(-1,-5,-1):
            if a[i][j]!="    ":
                if a0 != a[i][j]:
                    a0=a[i][j]
                    a[pos1][j],a[i][j]=a[i][j],a[pos1][j]
                    pos1-=1
                else:
                    a[pos1+1][j]=str(int(a[pos1+1][j])*2)+(4-len(str(int(a[pos1+1][j])*2)))*" "
                    a[i][j]="    "
                    a0=a[pos1+1][j]
                    num+=1
            else:
                num+=1
    return num
def move_a():
    num=0
    for i in range(4):
        a0=""
        pos1=1
        for j in range(1,9,2):
            if a[i][j]!="    ":
                if a0 != a[i][j]:
                    a0=a[i][j]
                    a[i][pos1],a[i][j]=a[i][j],a[i][pos1]
                    pos1+=2
                else:
                    a[i][pos1-2]=str(int(a[i][pos1-2])*2)+(4-len(str(int(a[i][pos1-2])*2)))*" "
                    a[i][j]="    "
                    a0=a[i][pos1-2]
                    num+=1
            else:
                num+=1
    return num
def move_d():
    num=0
    for i in range(4):
        a0=""
        pos1=-2
        for j in range(-2,-10,-2):
            if a[i][j]!="    ":
                if a0 != a[i][j]:
                    a0=a[i][j]
                    a[i][pos1],a[i][j]=a[i][j],a[i][pos1]
                    pos1-=2
                else:
                    a[i][pos1+2]=str(int(a[i][pos1+2])*2)+(4-len(str(int(a[i][pos1+2])*2)))*" "
                    a[i][j]="    "
                    a0=a[i][pos1+2]
                    num+=1
            else:
                num+=1
    return num

a=[];b=[]
for i in range(4):
    flag=1
    a.append([])
    b.append([])
    for j in range(9):
        if flag:
            a[i].append("|")
            b[i].append("|")
        else:
            a[i].append("    ")
            b[i].append("    ")
        flag=1-flag
        
a[randint(0,3)][randint(0,3)*2+1]="2   "
if_add=1
kongge=16
while 1:
    flag=1
    for i in range(4):
        for j in range(1,9,2):
            if a[i][j]=="    ":
                flag=0
    if flag:
        break
    site=0
    pos2=randint(1,kongge)
    if if_add:
        for i in range(4):
            flag=0
            for j in range(1,9,2):
                if a[i][j]=="    ":
                    site+=1
                if site==pos2:
                    a[i][j]="2   "
                    flag=1
                    break
            if flag:
                break
    for i in range(4):
        for j in range(9):
            print(a[i][j],end="")
            b[i][j]=a[i][j]
        print("")
    movement=input("w/a/s/d to move:")
    if movement=="w":
        move_w()
        move_w()
        kongge=move_w()
    elif movement=="s":
        move_s()
        move_s()
        kongge=move_s()
    elif movement=="a":
        move_a()
        move_a()
        kongge=move_a()
    elif movement=="d":
        move_d()
        move_d()
        kongge=move_d()
    if a==b:
        if_add=0
    else:
        if_add=1
                        