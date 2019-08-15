import pygame
from pygame.sprite import spritecollide
from collections import deque
from random import randint, randrange
from .sprites.snake import Snake, SnakePart
from .sprites.food import Food


class Game:
    def __init__(self, width=640, height=460):
        self.size = self.width, self.height = width, height
        self.all_sprites = pygame.sprite.Group()
        self.food_group = pygame.sprite.Group()
        self.snake = None
        self.surface = None
        self.running = False

    def get_random_block(self):
        return randrange(self.width//10)*10, randrange(self.height//10)*10
        
    def start(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(size=self.size)
        self.running = True

    def stop(self):
        self.running = False
    
    def update(self):
        self.snake.move()
        self.all_sprites.update()

        for sprite in spritecollide(self.snake.head, self.food_group, dokill=True):
            self.food_group.add(Food(pos=self.get_random_block()))
            self.snake.grow(sprite.color)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.snake.head.direction=(0, 1)
            if event.key == pygame.K_UP:
                self.snake.head.direction=(0, -1)
            if event.key == pygame.K_RIGHT:
                self.snake.head.direction=(1, 0)
            if event.key == pygame.K_LEFT:
                self.snake.head.direction=(-1, 0)

    def run(self):
        self.start()
        
        # define sprites and groups
        self.food_group = pygame.sprite.Group()
        self.snake = Snake()
        for _ in range(3):
            self.snake.grow()

        self.food_group.add(Food(pos=self.get_random_block()))

        # define clock
        clock = pygame.time.Clock()

        while self.running:
            
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                self.handle_event(event)
           
            # update all sprites
            self.all_sprites.add(self.snake.head, *self.snake.tail, self.food_group)
            self.update()

            self.all_sprites.draw(self.surface)
            pygame.display.flip()

            clock.tick(20)
