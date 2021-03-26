import pygame 

class Map:
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.grid = []
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dungeon Generator with Pygame")
        
        for w in range(self.width // 2):
            temp = []
            for h in range(self.height // 2):
                temp.append(pygame.Rect((2 * w, 2 * h), (2,2)))
                # pygame.draw.rect(self.screen, Map.RED, self.grid[w][h])
            self.grid.append(temp)