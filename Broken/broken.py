# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
from pygame.locals import *
import sys
from line import Line
from time import time
# from background import Background
from tap import Tap
from settings import Settings

tap_site = [[1,0,1000],
            [1,1,2000],
            [1,2,3000],
            [1,3,4000],
            [1,0,10000]]
# orwd = 350

class Broken:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.alltap = []
        self.will_kill_taps = pygame.sprite.Group()
        self.lines = pygame.sprite.Group()
        for i in range(4):
            taps = pygame.sprite.Group()
            self.alltap.append(taps)
            
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Broken")
#         self.bg_color = (0,0,0)

        self.clock = pygame.time.Clock()
        
        
        
    def run_game(self):
        # new_line = Line(self)
        # self.lines.add(new_line)
        # self._the_backgroud()
        wide = self.settings.wide
        i = 0 
        to_score = [0,0,0,0]
        
        while True:
            self.clock.tick(60)
            
            if_kill = [0,0,0,0]
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # if event.key in self.settings.original_keys[0] and if_to_score[0]:
                    for j in range(4): 
                        if event.key in self.settings.original_keys[j] and to_score[j]:
                            # 加分
                            # print(event.key,self.settings.original_keys[j],to_score[j])
                            if_kill[j] = 1
                        
                            # # self.alltap[j].remove(self.alltap[j][0])
                            # for tap in self.alltap[j].copy():
                            #     self.alltap[j].remove(tap)
                            # #依据to_score的相关数值加分,之后数值归零#if_to_score与to_score功能合一，添加if_kill列表
                            # to_score[j] = if_to_score[j] = 0
                            #改为改变if_kill列表中的相应参数，下方判定遍历中sprites改为copy，发现本列if_kill参数改变后删除本列首项精灵，再改变if_kill参数
            
            self.screen.fill(self.settings.bg_color)
            self._the_backgroud()
            
            if i < len(tap_site):
                i = self.update_taps(wide,i)
            for j in range(len(self.alltap)):
                if to_score[j] == 4:
                    if_kill[j] = 1  #若toscore显示为miss，则预备删除
                for tap in self.alltap[j].sprites():
                    tap.draw_tap()
            # print(len(self.taps))
            
            self._rollingline()
            self.lines.update()
            to_score = [0,0,0,0]
            for line in self.lines.sprites():
                if self.settings.inner_h < line.rect.y <=  self.settings.inner_h+self.settings.wide:
                    wide += self.settings.line_speed
                
                for j in range(len(self.alltap)):
                    if not if_kill[j]:
                        self._traversal_tap_sprites(j,line,to_score)
                    else:
                        self. _traversal_tap_copy(j,line,to_score,if_kill)
                        
                line.draw_line()
            
            # for part in self.bg.sprites():
            #     part.draw_bg()
            
            pygame.display.flip()
            
    def _rollingline(self):
        if len(self.lines)==0:
            line_a = Line(self,0,0)
            self.lines.add(line_a)
            new_line = Line(self,0-self.settings.wide,1)
            new_line.rect.bottom = self.settings.screen_height-self.settings.wide*2
            self.lines.add(new_line)
        # for line in self.lines.copy():
        #     if (line.rect.bottom >= self.settings.wide and len(self.lines) == 1) or len(self.lines)==0:
        #         new_line = Line(self)
        #         self.lines.add(new_line)
        #     elif line.rect.bottom >= self.settings.screen_height:
        #         self.lines.remove(line)
        # n = 0
        for line in self.lines.sprites():
            if line.rect.bottom >= self.settings.screen_height:
                line.rect.bottom = line.y = self.settings.screen_height-self.settings.wide*2
                line.n += 2
            
                # print(time())
#             print(line.rect.bottom,n)
            # n = 1-n
        # print(len(self.lines))
        
    def _the_backgroud(self):
        # rect_y = self.settings.inner_h
        # for i in range(k):
        #     a_part = Background(self)
        #     a_part.rect.x += (self.settings.bgrect_w + self.settings.bgrect_s)*i
        #     a_part.rect.y = rect_y
        #     self.bg.add(a_part)
        rect1 = pygame.Rect(0,self.settings.inner_h,self.settings.bgrect_w,self.settings.bgrect_h)
        pygame.draw.rect(self.screen,self.settings.bgrect_c,rect1)
        # rect_y += self.settings.wide
        # for i in range(k):
        #     a_part = Background(self)
        #     a_part.rect.x += (self.settings.bgrect_w + self.settings.bgrect_s)*i
        #     a_part.rect.y = rect_y
        #     self.bg.add(a_part)
        rect2 = pygame.Rect(0,self.settings.inner_h+self.settings.wide,self.settings.bgrect_w,self.settings.bgrect_h)
        pygame.draw.rect(self.screen,self.settings.bgrect_c,rect2)
            
    def update_taps(self,wide,i):
        # print(i)
        for site_index in range(i,len(tap_site)):
            x = tap_site[site_index][1]*self.settings.screen_width//4+50
            y = tap_site[site_index][2]*self.settings.tap_speed
            if y <= wide:
                a_tap = Tap(self,x,y%self.settings.wide+125,y//self.settings.wide)
                self.alltap[tap_site[site_index][1]].add(a_tap)
                # print(len(self.alltap[tap_site[site_index][1]]),y//self.settings.wide%2)
            else:
                i = site_index
                return i
        return len(tap_site)
    
    def _traversal_tap_sprites(self,j,line,to_score):
        for tap in self.alltap[j].sprites():
            if line.n != tap.n:
                continue
            if tap.rect.y - self.settings.judge_wide3 <= line.rect.y <= tap.rect.y + self.settings.judge_wide3:
                # print(3)
                if not to_score[j]:
                    to_score[j] = 3
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y - self.settings.judge_wide2 <= line.rect.y <= tap.rect.y + self.settings.judge_wide2:
                # print(2)
                if not to_score[j]:
                    to_score[j] = 2
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y - self.settings.judge_wide1 <= line.rect.y <= tap.rect.y + self.settings.judge_wide1:
                # print(1)
                if not to_score[j]:
                    to_score[j] = 1
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y + self.settings.judge_wide1 < line.rect.y:
                # print("miss")
                to_score[j] = 4
                self.will_kill_taps.add(tap)
           
        # print(to_score)
        return to_score
            
    def _traversal_tap_copy(self,j,line,to_score,if_kill):
        for tap in self.alltap[j].copy():
            if tap in self.will_kill_taps:
                self.alltap[j].remove(tap)
                self.will_kill_taps.remove(tap)
                if_kill[j] = 0
                # print(len(self.alltap[j]))
                continue
            if line.n != tap.n:
                continue
            if tap.rect.y - self.settings.judge_wide3 <= line.rect.y <= tap.rect.y + self.settings.judge_wide3:
                if not to_score[j]:
                    to_score[j] = 3
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y - self.settings.judge_wide2 <= line.rect.y <= tap.rect.y + self.settings.judge_wide2:
                if not to_score[j]:
                    to_score[j] = 2
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y - self.settings.judge_wide1 <= line.rect.y <= tap.rect.y + self.settings.judge_wide1:
                if not to_score[j]:
                    to_score[j] = 1
                    self.will_kill_taps.add(tap)
                else:
                    continue
            if tap.rect.y + self.settings.judge_wide1 < line.rect.y:
                to_score[j] = 4
                self.will_kill_taps.add(tap)
                # self.alltap[j].remove(tap)
           
        # print(to_score)
        return to_score,if_kill
    
if __name__ == '__main__':
    ai = Broken()
    ai.run_game()