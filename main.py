import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    # Clock and delta time for FPS
    clock = pygame.time.Clock()
    dt = 0
    # Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
 


    # Game Loop
    while True:
        # Enables the ability to press the [X] button at the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #hook player rotate from player.py
        player.update(dt)
        # Screen Fill
        screen.fill("black")
        # drawing player in game
        player.draw(screen)
        pygame.display.flip()
        # Framerate limiter to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
