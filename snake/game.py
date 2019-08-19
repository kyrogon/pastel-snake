import pygame
from pygame.sprite import spritecollide
from collections import deque
from random import randint, randrange

from .sprites.snake import Snake
from .sprites.food import Food


class Game:
    def __init__(self, width=640, height=448):
        self.size = self.width, self.height = width, height
        self.all_sprites = pygame.sprite.Group()
        self.food_group = pygame.sprite.Group()
        
        self.snake: pygame.sprite.Group = None
        self.surface = None
        self.running = False

    def start(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(size=self.size)
        self.running = True

    def stop(self):
        self.running = False
    
    def update(self):
        if self.snake.sprites():
            for sprite in spritecollide(self.snake.sprites()[0], 
                                        self.food_group, dokill=True):
                self.snake.grow(sprite.color)
                new_food = Food()
                new_food.place(self.width, self.height)
                self.food_group.add(new_food)

        self.all_sprites.add(self.food_group, self.snake)
        self.snake.update()
        self.all_sprites.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.snake.direction=(0, 1)
            if event.key == pygame.K_UP:
                self.snake.direction=(0, -1)
            if event.key == pygame.K_RIGHT:
                self.snake.direction=(1, 0)
            if event.key == pygame.K_LEFT:
                self.snake.direction=(-1, 0)

    def run(self):
        self.start()
        
        # define sprites and groups
        self.food_group = pygame.sprite.Group()
        self.snake = Snake()
        
        new_food = Food()
        new_food.place(self.width, self.height)
        self.food_group.add(new_food)

        # define clock
        clock = pygame.time.Clock()

        while self.running:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                self.handle_event(event)
           
            # update all sprites
            self.update()

            self.all_sprites.draw(self.surface)
            pygame.display.flip()

            clock.tick(15)
