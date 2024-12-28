# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:42:59 2022

@author: mac
"""

import pygame
from pygame.sprite import Sprite
from settings import Settings

class Background(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.settings = Settings()
        self.screen = ai_game.screen
        self.color = self.settings.bgrect_c
        self.rect = pygame.Rect(0,0,self.settings.bgrect_w,self.settings.bgrect_h)
        
    def draw_bg(self):
        pygame.draw.rect(self.screen,self.color,self.rect)