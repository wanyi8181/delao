import pygame
from pygame._sprite import Sprite


class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
       #
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()


        screen_rect = ai_game.screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        #
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        #
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)