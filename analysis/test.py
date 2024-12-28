# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:48:53 2022

@author: Administrator
"""

from PIL import Image as im
img=im.open("none.bmp")
print(img.size)
img.show()