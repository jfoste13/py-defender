import pygame, sys
from helper import *
from game_objects import *

def main():

    pygame.init()

    # handles all gameplay related variables
    game = GameVariables(True)
    game.max_asteroids = 10
    game.asteroid_size_range = [20, 50]
    game.asteroid_speed_range = [1, 3]
    game.gravity = .05
    game.ground_level = 10

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
        populateAsteroids(game, asteroid_list)
        ### DRAWING ###
        screen.fill(BLACK)
        asteroid_list.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        fpsclock.tick(TICK_RATE)

if __name__ == '__main__':
    main()
