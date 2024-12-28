# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:12:41 2023

@author: HUAWEI2
"""

from random import randint
bottles = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[0,0,0,0]]
top = [3,3,3,-1]

def get_num(ist):
    num = 1
    for i in range(top[ist],0,-1):
        if bottles[ist][i] == bottles[ist][i-1]:
            num += 1
        else:
            break
    return num

def pour(ist,t_ist,m):
    # print(m)
    while m>0:
        top[t_ist]+=1
        bottles[t_ist][top[t_ist]] = bottles[ist][top[ist]]
        bottles[ist][top[ist]] = 0
        top[ist]-=1
        m-=1
    show()    
    
def show():
    for i in range(3,-1,-1):
        for j in range(len(bottles)):
            print(bottles[j][i],end='\t')
        print()
    print('____________________')

def judge():
    for i in range(len(bottles)):
        for j in range(2,-1,-1):
            if bottles[i][j] != bottles[i][j+1]:
                return False
    return True

pos = randint(0,len(bottles)-2)
f = 0
while f<4:
    t = get_num(pos)
    if t==1 and top[pos]>0 or top[pos]<0:
        f+=1
        pos = (pos+1)%len(bottles)
        continue
    if t==top[pos]+1:
        move = int(randint(1,t**2)**(1/2))
    else:
        move = int(randint(1,(t-1)**2)**(1/2))
    # print(move)
    nmax = 0;imax = -1
    for i in range(1,4):
        itp = (pos+i)%len(bottles)
        if top[itp] == -1 or 3-top[itp] >= move and bottles[itp][top[itp]] != bottles[pos][top[pos]]:
            pour(pos, itp, move)
            pos = (pos+1)%len(bottles)
            f = -1
            break
        elif 3-top[itp] > nmax:
            nmax = 3-top[itp]
            imax = itp
    else:
        if nmax > 0 and bottles[imax][top[imax]] != bottles[pos][top[pos]]:
            pour(pos,imax,nmax)
            pos = (pos+1)%len(bottles)
            f = 0
            continue
    if f == -1:
        f = 0
    else:
        f+=1

show()
while not judge():
    i_out = int(input("out"))
    i_in = int(input("in"))
    if bottles[i_in][top[i_in]] != bottles[i_out][top[i_out]] and top[i_in] != -1:
        print('False!')
        continue
    while top[i_out] >=0 and top[i_in]<3 and bottles[i_out][top[i_out]] == bottles[i_in][top[i_in]]:
        top[i_in] += 1
        bottles[i_in][top[i_in]] = bottles[i_out][top[i_out]]
        bottles[i_out][top[i_out]] = 0
        top[i_out] -= 1
    show()