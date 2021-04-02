import pygame


class Tile:
    w = 25
    h = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filepath = None
        self.imgLoaded = pygame.image.load(self.filepath)

    def draw(self, windows):
        windows.blit(self.imgLoaded, (self.x, self.y))
