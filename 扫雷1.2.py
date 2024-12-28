import random as rd

wid=int(input("width="))
hei=int(input("height="))
num=int(input("number of booms="))
a=[]
b=[]

a=[["■" for i in range(wid)] for j in range(hei)]
b=[[0 for i in range(wid)] for j in range(hei)]
    
def delete(y,x):           #delete
    d=0
    for i in range(max(y-1,0),min(y+2,hei)):
        for j in range(max(x-1,0),min(wid,x+2)):
            if b[i][j]:
                d+=1
    a[y][x]=str(d)
    if d==0:
        for i in range(max(y-1,0),min(y+2,hei)):
            for j in range(max(x-1,0),min(wid,x+2)):
                if a[i][j]=="■":
                    delete(i,j)
#     t=a[y][x]

def print_map(hei,wid):
    for i in range(hei):
        print("│",end="")   
        for j in range(wid):
            print(" "+a[i][j]+" ",end="│")
        print("\n")


a[hei//2][wid//2]="□"
wjy=hei//2
wjx=wid//2
t="■"
z=0

while 1:
    a[wjy][wjx]="□"
    '''
    for i in range(hei):
        print("│",end="")   
        for j in range(wid):
            print(" "+a[i][j]+" ",end="│")
        print("\n")
    '''
    print_map(hei,wid)
    movement=input("wasd move/z or zz delete/x sign=")
    
    if movement=="w"and wjy>0:      #上移
       a[wjy][wjx]=t
       t=a[wjy-1][wjx]
       wjy-=1
    
    elif movement=="s"and wjy<hei-1:    #下移
       a[wjy][wjx]=t
       t=a[wjy+1][wjx]
       wjy+=1
    
    elif movement=="a"and wjx>0:    #左移
        a[wjy][wjx]=t
        t=a[wjy][wjx-1]
        wjx-=1
    
    elif movement=="d"and wjx<wid-1:    #右移
        a[wjy][wjx]=t
        t=a[wjy][wjx+1]
        wjx+=1
    
    elif movement=="z" and (t=="■"or t=="♦"):   #删除
        z+=1
        if z==1:
            i=0
            while i<num:       #create the spot of booms 
                x=rd.randint(0,wid-1)
                y=rd.randint(0,hei-1)
                if b[y][x]==0 and (x not in range(wjx-1,wjx+2) or y not in range(wjy-1,wjy+2)):
                    b[y][x]=1
                else:
                    i-=1
                i+=1
        if b[wjy][wjx]:
            print("failure")
            for i in range(hei):
                for j in range(wid):
                    print(str(b[i][j])+"   ",end="")
                print("\n")
            break
        else:
            delete(wjy,wjx)
            r=0
            for i in range(max(wjy-1,0),min(wjy+2,hei)):
                for j in range(max(wjx-1,0),min(wid,wjx+2)):
                    if b[i][j]==1:
                        r+=1
            t=str(r)
        k=0
        for i in range(hei):
            for j in range(wid):
                if a[i][j]=="■"or a[i][j]=="♦":
                    k+=1
        if k==num:
            print_map(hei,wid)
            print("victory")
            break
    
    elif movement=="x"and t=="■":
        t="♦"
   
    elif movement=="zz" and "0"<=t<="9":
        n=0
        for i in range(max(wjy-1,0),min(wjy+2,hei)):
            for j in range(max(wjx-1,0),min(wid,wjx+2)):
                if a[i][j]=="♦":
                    n+=1
        if n==int(t):
            for i in range(max(wjy-1,0),min(wjy+2,hei)):
                for j in range(max(wjx-1,0),min(wid,wjx+2)):
                    if a[i][j]=="■":
                        delete(i,j)
        k=0
        for i in range(hei):
            for j in range(wid):
                if a[i][j]=="■"or a[i][j]=="♦":
                    k+=1
        if k==num:
            print_map(hei.wid)
            print("victory")
            break
        
        
        
        
    
