import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # Enables the ability to press the [X] button at the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Screen Fill
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
