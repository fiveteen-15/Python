# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=[];b=[]
for i in range(4):
    flag=1
    a.append([])
    
    for j in range(9):
        if flag:
            a[i].append("|")
            
        else:
            a[i].append("    ")
            
        flag=1-flag
movement=input("w/a/s/d to move:")
dicx={'a':2,'d':-2,'w':0,'s':0}
dicy={'a':0,'d':0,'w':1,'s':-1}
def move_w(shuru):
    num=0
    for j in range(1,9,2):
        a0=""
        posx=0
        posy=0
        for i in range(4):
            if a[i][j]!="    ":
                if a0 != a[i][j]:
                    a0=a[i][j]
                    a[pos1][j],a[i][j]=a[i][j],a[pos1][j]
                    posx+=dicx[shuru]
                else:
                    a[pos1-1][j]=str(int(a[pos1-1][j])*2)+(4-len(str(int(a[pos1-1][j])*2)))*" "
                    a[i][j]="    "
                    a0=a[pos1-1][j]
                    num+=1
            else:
                num+=1
    return num