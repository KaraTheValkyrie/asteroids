# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this imports some variables that
# we declare in another file
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # handle exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #render a black screen
        screen.fill(000000)
        pygame.display.flip()


if __name__ == "__main__":
    main()
