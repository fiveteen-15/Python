# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:13:53 2023

@author: HUAWEI2
"""
from draw_line import draw_line

class main():
    
    def __init__(self):
        v_r = 5
        k = 3**0.5/3
        l = 10 #透视点距离
        self.v_d = [k,k,k]
        self.v_center = [self.v_d[0]*v_r,self.v_d[1]*v_r,self.v_d[2]*v_r]
        self.v_focus = [self.v_d[0]*l,self.v_d[1]*l,self.v_d[2]*l]
        t = (self.v_d[0]**2+self.v_d[1]**2)**0.5
        self._x0 = [(-1)*self.v_d[1],self.v_d[0],0]
        self._y0 = [(-1)*self.v_d[2]*self.v_d[0]/t,(-1)*self.v_d[2]*self.v_d[1]/t,t]
    def dr_subtract(a1,a2):
        a = [0,0,0]
        for i in range(3):
            a[i] = a1[i] - a2[i]
        return a
    def dr_multiple(a1,a2):
        a = 0
        for i in range(3):
            a += a1[i] * a2[i]
        return a
    def drnum_multiple(n,a1):
        a = [0,0,0]
        for i in range(3):
            a[i] = n*a1[i]
        return a
    def dr_sum(a1):
        return (a1[0]**2+a1[1]**2,a1[2]**2)**0.5
    def reflect(self,pos,v_center,v_focus,v_d,_x0,_y0):
        _pc = self.dr_subtract(v_center, pos)
        ph = self.dr_multiple(_pc, v_d)
        if ph < 0:
            return
        _ph = self.drnum_multiple(ph, v_d)
        _ch = self.dr_subtract(_ph, _pc) 
        cf = self.dr_sum(self.dr_subtract(v_focus, v_center))
        _cs = self.drnum_multiple(cf/(cf+ph), _ch)
        x = self.dr_multiple(_cs, _x0)
        y = self.dr_multiple(_cs, _y0)
        return [x,y]