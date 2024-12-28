# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:38:48 2022

@author: mac
"""
import pygame
from pygame.sprite import Sprite

class Line(Sprite):
    
    def __init__(self,ai_game,y,n):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.line_color
        self.rect = pygame.Rect(0,y,self.settings.line_width,self.settings.line_height)
#         self.midbottom = 0
        self.y =float(self.rect.y)
        self.n = n
        
    def update(self):
        self.y += self.settings.line_speed
        self.rect.y = self.y
        
    def draw_line(self):
        pygame.draw.rect(self.screen,self.color,self.rect)