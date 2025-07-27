# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this imports code that we have
# saved in other files
from constants import *

from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialize things and set the screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set some variables to control the game's FPS
    clock = pygame.time.Clock()
    dt = 0

    # create the player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        #handle exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #render a black screen
        screen.fill(000000)

        #render the player
        player.draw(screen)

        #update the display
        pygame.display.flip()

        #tell the game to wait 1/60 of a second
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
