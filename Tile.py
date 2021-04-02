import pygame


class Tile:
    w = 25
    h = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filepath = None
        self.imgLoaded = None

    def draw(self, windows):
        windows.blit(self.imgLoaded, (self.x, self.y))

    def setFilePath(self, filePath):
        self.filepath = filePath

    def loadImage(self):
        if self.filepath:
            self.imgLoaded = pygame.image.load(self.filepath)
        else:
            print("FILE PATH IS NONE")
            SystemExit()
