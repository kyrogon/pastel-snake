import pygame
from collections import deque
from pygame.sprite import Sprite, Group


class Snake:
    def __init__(self):
        self.head = SnakePart()
        self.tail = deque()

    def grow(self, color=(255, 255, 255)):
        self.tail.append(
            SnakePart(
                pos=self.head.pos,
                color=color,
            )
        )
    
    def move(self):
        self.tail.rotate(-1)
        self.tail[0].pos = self.head.pos
        self.head.move()

class SnakePart(Sprite):
    def __init__(self, pos=(0, 0), color=(255, 255, 255), size=10):
        super().__init__()

        self.size = size

        self.image = pygame.Surface([size, size])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.pos = pos

        self.position_history = []

        self.direction = (0, 0)


    @property
    def pos(self):
        return self.rect.x, self.rect.y

    @pos.setter
    def pos(self, pos):
        self.rect.x, self.rect.y = pos

    def move(self):
        self.rect.x += self.direction[0] * self.size
        self.rect.y += self.direction[1] * self.size

