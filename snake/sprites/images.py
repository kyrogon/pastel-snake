import pygame

class TileSet:
    def __init__(self, filename, tile_size=64):
        self.tile_size = tile_size
        self.tile_sheet = pygame.image.load(filename)
    
    def get_tile(self, x, y):
        location = x * self.tile_size, y * self.tile_size
        return self.tile_sheet.subsurface(
            pygame.Rect(location, (self.tile_size, self.tile_size))
        )
