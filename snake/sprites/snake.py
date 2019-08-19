import pygame
from operator import add
from itertools import starmap
from pygame.sprite import Sprite, Group
import numpy as np
from .images import TileSet


class Snake(Group):
    def __init__(self, start_length=3):
        super().__init__()

        # process arguments into instance attributes
        self._start_length = start_length
        self.direction = (1, 0)

        head = SnakeBit()
        head.section = 'head'
        head.direction = self.direction
        self.add(head)
        
    def update(self):
        if len(self.sprites()) < 3:
            self.grow()
        self.move()

    def move(self):
        if not self.sprites():
            return None
        head = self.sprites()[0]
        tail = self.sprites()[-1]

        new_pos = head.pos
        new_dir = head.direction

        head.direction = self.direction
        head.move(self.direction)

        for sprite in self.sprites()[1:]:
            tmp_new_pos = sprite.pos
            tmp_new_dir = sprite.direction

            sprite.pos = new_pos
            sprite.direction = new_dir

            new_pos = tmp_new_pos
            new_dir = tmp_new_dir

    def grow(self, color=(255, 255, 255)):
        old_tail = self.sprites()[-1]
        new_sprite = SnakeBit(color=color)
        if self.sprites():
            new_sprite.section = 'tail'
            new_sprite.pos = self.sprites()[-1].pos
            new_sprite.direction = self.sprites()[-1].direction
        if old_tail.section != 'head':
            old_tail.section = 'body'
        self.add(new_sprite)
        

class SnakeBit(Sprite):
    images = TileSet('snake/imgs/snake_tiles.png')
    tiles = {
        'head': {
            (1, 0):  (4, 0),
            (-1, 0): (3, 1),
            (0, -1): (3, 0),
            (0, 1):  (4, 1),
        },
        'tail': {
            (1, 0):  (4, 2),
            (-1, 0): (3, 3),
            (0, -1): (3, 2),
            (0, 1):  (4, 3),
        },
        'body': {
            (1, 0):  (1, 0),
            (-1, 0): (1, 0),
            (0, -1): (2, 1),
            (0, 1):  (2, 1),
        },
    }
   
    def __init__(self, size=16, pos=(0, 0), color=(255, 255, 255)):
        super().__init__()
        
        self.size = size
        self.image = pygame.Surface((self.size, self.size))

        self.rect = self.image.get_rect()
        self.pos = pos
        self.section = None
        self.direction = (1, 0)

    @property
    def pos(self):
        return self.rect.x, self.rect.y

    @pos.setter
    def pos(self, value):
        self.rect.x, self.rect.y = value

    def move(self, direction):
        direction = tuple(d * self.size for d in direction)
        self.pos = starmap(add, zip(self.pos, direction))

    def change_image(self, section, direction):
        self.image.fill((0, 0, 0))
        image = self.images.get_tile(*self.tiles[section][direction])
        image = pygame.transform.scale(image, (self.size, self.size))
        self.image.blit(image, (0, 0))

    def update(self):
        self.change_image(self.section, self.direction)
