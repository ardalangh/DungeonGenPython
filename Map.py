import pygame

from Tile import Tile


class Map:
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.tiles = [[None * self.height // 50] * self.width // 25]
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dungeon Generator with Pygame")


        for x in self.width:
            for y in self.height:
                self.tiles[x][y] = Tile(x * 25, y * 50)

    def draw(self, window):
        for tile in self.tiles:
            tile.draw(window)

        

                
