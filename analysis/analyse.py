#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image as im
from PIL import ImageTk 
import numpy as np



dic_plot={"plot1":"x","plot2":"lnx","plot3":"(x+c)^2","plot4":"/x"} #c的值之后再想办法

def do_r(x,y):
#     global x,y,x_mean,y_mean
#     flag=1
#     x=[]
#     y=[]
    for i in range(len(x)):
        x[i]=int(x[i])
        y[i]=int(y[i])
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    sum1=0
    for i in range(len(x)):
        sum1+=(x[i]-x_mean)*(y[i]-y_mean)
    sum2=0
    for i in x:
        sum2+=(i-x_mean)**2
    else:
        sum2=sum2**(1/2)
    sum3=0
    for i in y:
        sum3+=(i-y_mean)**2
    else:
        sum3=sum3**(1/2)
    return sum1/sum2/sum3
# s=[40,150,42,140,48,160,55,170,65,150,79,162,88,185,100,165,120,190,140,185]
# print(do_r(s))

def calculate(x,y):
    
    b1=0;b2=0;a=b=0
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    for i in range(len(x)):
        b1=b1+x[i]*y[i]-x_mean*y_mean
        b2=b2+x[i]**2-x_mean**2
    b=b1/b2
    a=y_mean-b*x_mean
    return a,b

def draw(x,y,a,b,kind):
    x_min=min(x)-(max(x)-min(x))//5
    x_max=max(x)+(max(x)-min(x))//5
    # print(x_min,x_max)
    x0=np.linspace(x_min,x_max,50)
    y0=[]
    if kind=="plot1":
        for i in range(50):
            y0.append(x0[i]*b+a)
    elif kind=='plot2':
        for i in range(50):
            y0.append(np.log(x0[i])*b+a)
    plt.rcParams["font.family"]="SimHei"
    plt.rcParams["axes.unicode_minus"]=False
    plt.figure()
    plt.plot(x0,y0,label="y=%.3f"%b+dic_plot[kind]+"+%.3f"%a)
    # print(x0,y0)
    plt.scatter(x, y, label="样本数据")
    # plt.ylim(min(x_min*b+a,x_max*b+a),max(x_min*b+a,x_max*b+a))
    # plt.xlim(x_min,x_max)
    plt.legend()
    plt.savefig("plotfigure.jpg")
    # plt.show()
def pic_plot1(x,y):
    
    for i in range(len(x)):
        x[i]=int(x[i])
        y[i]=int(y[i])
    a,b=calculate(x, y)
    draw(x,y,a,b,"plot1")   #x0按x均匀取值，y0按x均匀取值
    img=im.open("plotfigure.jpg")
    weight,height=img.size
    img=ImageTk.PhotoImage(img)
    return img,weight,height,a,b

def pic_plot2(x,y):
    lnx=[]
    for i in range(len(x)):
        x[i]=int(x[i])
        lnx.append(np.log(x[i]))
        y[i]=int(y[i])
    a,b=calculate(lnx, y)
    draw(x,y,a,b,"plot2")   #x0按x均匀取值，y0按lnx均匀取值
    img=im.open("plotfigure.jpg")
    weight,height=img.size
    img=ImageTk.PhotoImage(img)
    return img,weight,height,a,b

def residuals(a,b,x,y,kind):
    re_y=[]
    if kind=='y=bx+a':
        for i in range(len(x)):
            re_y.append(y[i]-(x[i]*b+a))
    elif kind=='y=blnx+a':
        for i in range(len(x)):
            re_y.append(y[i]-(np.log(x[i])*b+a))
    # print(x,re_y)
    plt.rcParams["font.family"]="SimHei"
    plt.figure()
    plt.scatter(x,re_y)
    # print(x0,y0)
    ax=plt.gca()
    ax.spines['right'].set_color('none')#去掉右边边框
    ax.spines['top'].set_color('none')#去掉上方边框
    ax.xaxis.set_ticks_position('bottom')#把x轴的刻度设置为‘bottom’，x轴刻度上的字都在x轴下部
    ax.yaxis.set_ticks_position('left')#把y轴的刻度设置为‘left’，y轴刻度上的字都在y轴左部
    ax.spines['bottom'].set_position(('data',0))#设置x轴位置，让x轴位于0的位置
    # ax.spines['left'].set_position(('data',0))#设置y轴位置，让y轴位于0的位置
    # plt.ylim(min(x_min*b+a,x_max*b+a),max(x_min*b+a,x_max*b+a))
    # plt.xlim(x_min,x_max)
    plt.savefig("residuals.jpg")
    plt.show()
    img0=im.open("residuals.jpg")
    weight0,height0=img0.size
    img0=ImageTk.PhotoImage(img0)
    return img0,weight0,height0
    # plt.show()
# s=[40,150,42,140,48,160,55,170,65,150,79,162,88,185,100,165,120,190,140,185]
# flag=1
# x=[]
# y=[]
# for i in s:
#     if flag:
#         x.append(int(i))
#     else:
#         y.append(int(i))
#     flag=1-flag
# #print(do_r(s))
# img=pic(x,y)
# # img=im.open("plotfigure.gif")
# # img.show()