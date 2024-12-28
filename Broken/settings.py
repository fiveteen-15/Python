# import pygame
# from pygame.locals import *
class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.inner_h = 125
        self.wide = 350
        self.bgrect_c = (255,0,0)
        self.bgrect_w = 1000
        self.bgrect_h = 2
        self.bgrect_s = 5
        
        self.line_speed = 2
        self.line_color = (255,0,0)
        self.line_width = 1000
        self.line_height = 10
        
        self.tap_color = (0,255,0)
        self.tap_w = 100
        self.tap_h = 10
        self.tap_speed = 0.1
        
        self.judge_wide1 = 50
        self.judge_wide2 = 30
        self.judge_wide3 = 20
        
        self.original_keys = [[113,117],[119,105],[101,111],[114,112]]