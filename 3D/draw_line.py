# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:11:33 2023

@author: HUAWEI2
"""

class draw_line():
    
    def __init__(self):
        self.sp1 = [-1,-3]
        self.sp2 = [4,5]
        self.width = 400
        self.height = 300
        self.color = (255,255,255)
    
    def creat_line(p1,p2):
        k = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1]-p1[0]*k
        return k,b
    
    def draw(self,sp1,sp2):
        from PIL import Image 
        # im = Image.open("w.jpg")
        im= Image.new("RGB", (self.width, self.height), self.color)
            
        if sp1[0]>sp2[0]:
            sp1,sp2 = sp2,sp1
        o = [self.width//2,self.height//2]
        p1 = [o[0]+sp1[0]*10,o[1]-sp1[1]*10]
        p2 = [o[0]+sp2[0]*10,o[1]-sp2[1]*10]
        k,b = self.creat_line(p1,p2)
        pim = im.load()
        for x in range(max(p1[0],0),min(p2[0],self.width-1)+1):
            y = int(k*x+b)
            pim[x,y] = (0,0,0)
            
        im.save('D:/Download/Blender 3.1/w.jpg')
        im.show()
# draw_line()
    # def creat_line(p1,p2):
    #     k = (p2[1]-p1[1])/(p2[0]-p1[0])
    #     b = p1[1]-p1[0]*k
    #     return k,b