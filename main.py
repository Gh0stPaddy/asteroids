import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Screen closed check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    # Game Loop
    while True:
        pygame.Surface.fill(screen, (0,0,0))

if __name__ == "__main__":
    main()
