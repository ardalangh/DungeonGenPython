import pygame
from Map import Map

running = True 
map = Map (400, 400)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruunning = False
    WIDTH = 20
    HEIGHT = 20
    
    # This sets the margin between each cell
    MARGIN = 5

    pygame.draw.rect(map.screen,
                             Map.RED,
                             [(MARGIN + WIDTH) * 10 + MARGIN,
                              (MARGIN + HEIGHT) * 10 + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # map.screen.fill(Map.BLACK)

    
    clock.tick(60)
    pygame.display.flip()


pygame.quit()
