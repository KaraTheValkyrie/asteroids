# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this imports code that we have
# saved in other files
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

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

    #create some groups to organize everything
    updatable_objects = pygame.sprite.Group()
    drawable_objects = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #add everything to the relevant groups
    Player.containers = (updatable_objects, drawable_objects)
    Asteroid.containers = (updatable_objects, drawable_objects, asteroids)
    AsteroidField.containers = (updatable_objects)

    # create the player and asteroid field objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        #handle exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #render a black screen
        screen.fill(000000)

        #update the position and rotation for all objects
        updatable_objects.update(dt)

        #render all objects
        for item in drawable_objects:
            item.draw(screen)
        
        #update the display
        pygame.display.flip()

        #tell the game to wait 1/60 of a second
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
