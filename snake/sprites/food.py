import pygame
from random import randrange
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, size=16, pos=(0, 0)):
        super().__init__()
        self.size = size
        self.color = [randrange(256) for _ in range(3)]
        
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.pos = pos
        
    @property
    def pos(self):
        return self.rect.x, self.rect.y
    
    @pos.setter
    def pos(self, value):
        self.rect.x, self.rect.y = value

    def place(self, screen_width, screen_height):
        self.pos = (randrange(screen_width//self.size)*self.size, 
                    randrange(screen_height//self.size)*self.size)
