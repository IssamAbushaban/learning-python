import pygame

# initializing pygame
pygame.init()

# set the game window size
scrWidth  = 500
scrHeight = 500
screen = pygame.display.set_mode([scrWidth, scrHeight])

# track the game's running mode
running = True

# the game is enclosed in the loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # game content

    # fill the screen with a white background
    screen.fill((255,255,255))
    # add a circle to the center of the screen
    pygame.draw.circle(screen, (0,0,255),(scrWidth/2,scrHeight/2), (scrHeight/10) + 10)
    
    # update the screen!
    pygame.display.update()

pygame.quit()