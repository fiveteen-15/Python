import pygame
from pygame.sprite import Sprite
from settings import Settings

# tap_site = [[1,0,1000],
#             [1,1,2000],
#             [1,2,3000],
#             [1,3,4000]]

class Tap(Sprite):
    def __init__(self,ai_game,x,y,n):
        super().__init__()
        self.settings = Settings()
        self.screen = ai_game.screen
        self.color = self.settings.tap_color
        self.rect = pygame.Rect(0,0,self.settings.tap_w,self.settings.tap_h)
        self.rect.x = x
        self.rect.y = y
        self.n = n

    def draw_tap(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        