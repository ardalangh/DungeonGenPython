import pygame 

class Map:
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    def __init__(self, width, height):
        self.height = height
        self.width = width
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pygame.set_caption("DunGeon Generator with pygame")
