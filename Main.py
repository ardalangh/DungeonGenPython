import pygame
from Map import Map
from Tile import Tile

running = True
mapWindow = Map(600, 600)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # This sets the margin between each cell
    MARGIN = 5

    for x in range(mapWindow.width // 25):
        for y in range(mapWindow.height // 50):
            mapWindow.tiles[x][y].setFilePath("stoneWall_N.png")
    mapWindow.draw()







    # pygame.draw.rect(mapMange.screen,
    #                  Map.RED,
    #                  [(MARGIN + WIDTH) * 10 + MARGIN,
    #                   (MARGIN + HEIGHT) * 10 + MARGIN,
    #                   WIDTH,
    #                   HEIGHT])

    # map.screen.fill(Map.BLACK)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
