from Map import Map

running = True 
map = Map (400, 400)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruunning = False


            
    map.screen.fill(Map.BLACK)


    