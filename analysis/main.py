#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import analyse 
from PIL import Image as Im
from PIL import ImageTk

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        # global img
        self.init_window_name.title("工具")           #窗口名
        # self.init_window_name.geometry('500x300+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('680x660+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_x_label = Label(self.init_window_name, text="x")
        self.init_data_x_label.grid(row=0, column=0)
        self.init_data_y_label = Label(self.init_window_name, text="y")
        self.init_data_y_label.grid(row=0, column=2)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=4)
        self.log_label = Label(self.init_window_name, text="残差")
        self.log_label.grid(row=22, column=4)
        self.choose_label = Label(self.init_window_name,text="模型")
        self.choose_label.grid(row=36,column=0)
        #文本框
        self.init_data_Text_x = Text(self.init_window_name, width=12, height=35)  #原始数据x录入框
        self.init_data_Text_x.grid(row=1, column=0, rowspan=35,columnspan=2)
        self.init_data_Text_y = Text(self.init_window_name, width=12, height=35)  #原始数据y录入框
        self.init_data_Text_y.grid(row=1, column=2, rowspan=35,columnspan=2)
        self.result_data_Text = Frame(self.init_window_name, width=70, height=21)  #处理结果展示
        self.result_data_Text.grid(row=1, column=4, rowspan=21, columnspan=10)
        self.log_data_Text = Frame(self.init_window_name, width=70, height=21)  # 日志框
        self.log_data_Text.grid(row=23, column=4, rowspan=21, columnspan=10)
        # img=ImageTk.PhotoImage(im.open("plotfigure.jpg"))
        self.result_pic_plot=Label(self.result_data_Text,bg="white",width=65, height=15)
        self.result_pic_plot.pack(padx=10)
        self.result_pic_scatter=Label(self.log_data_Text,bg="white",width=65, height=15)
        self.result_pic_scatter.pack(padx=10)
        #下拉框
        comvalue=StringVar()
        self.str_trans_to_md5_combobox = ttk.Combobox(self.init_window_name,textvariable=comvalue)
        self.str_trans_to_md5_combobox['values']=("y=bx+a",'y=blnx+a')#,'y=b(x+c)^2+a','y=1/x')
        # self.str_trans_to_md5_combobox.current(0)
        # self.str_trans_to_md5_combobox.bind("<<ComboboxSelected>>",self.str_trans_to_md5)
        self.str_trans_to_md5_combobox.grid(row=36, column=1, columnspan=2,sticky=EW)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="计算", bg="lightblue",command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=37, column=1, columnspan=2,sticky=EW)


    #功能函数
    def str_trans_to_md5(self):
        global img_none,img_sc
        srcx = self.init_data_Text_x.get(1.0,END).strip().split("\n")
        srcy = self.init_data_Text_y.get(1.0,END).strip().split("\n")
        plot_kind=self.str_trans_to_md5_combobox.get()
        #print("src =",src)
        if len(srcx) == len(srcy):
             try:
                if plot_kind=="y=bx+a":
                    # r=analyse.do_r(srcx,srcy)
                    self.im,wide,high,a,b=analyse.pic_plot1(srcx,srcy)
                    self.result_pic_plot.config(image=self.im,width=wide,height=high)
                elif plot_kind=="y=blnx+a":
                    self.im,wide,high,a,b=analyse.pic_plot2(srcx,srcy)
                    self.result_pic_plot.config(image=self.im,width=wide,height=high)
                img_sc,wide0,high0=analyse.residuals(a,b,srcx,srcy,plot_kind)
                self.result_pic_scatter.config(image=img_sc,width=wide0,height=high0)
             except:
                img_none=Im.open("none.bmp")
                img_none=ImageTk.PhotoImage(img_none)
                self.result_pic_plot.config(image=img_none,width=432,height=288)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()