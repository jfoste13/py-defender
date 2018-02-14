import pygame, sys
from helper import *
from game_objects import *

def main():

    pygame.init()

    # handles all gameplay related variables
    game = GameVariables(True)
    game.max_asteroids = 10
    game.asteroid_size_range = [20, 50]
    game.gravity = 1
    game.ground_level = 30

    # holds a bunch of asteroids
    asteroid_list = pygame.sprite.Group()

    # everything is drawn to this surface
    screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    # handles framerate
    fpsclock = pygame.time.Clock()

    ### MAIN GAME LOOP ###
    while game.playing:

        ### INPUT ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        ### LOGIC ###
        for asteroid in asteroid_list:
            asteroid.update()
            if asteroid.ground_contact:
                #asteroid_list.remove(asteroid)
                pass
        populateAsteroids(game, asteroid_list)
        ### DRAWING ###
        screen.fill(BLACK)
        asteroid_list.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        fpsclock.tick(TICK_RATE)

if __name__ == '__main__':
    main()
