import pygame, sys
from helper import *
from game_objects import *

def main():

    pygame.init()

    # handles all gameplay related variables
    game = GameVariables(True)
    game.max_asteroids = 10
    game.asteroid_size_range = [20, 50]
    game.gravity = .05
    game.ground_level = 10
    game.asteroid_spawn_cooldown = 60
    game.asteroid_spawn_counter = 0

    # holds a bunch of asteroids
    asteroid_list = pygame.sprite.Group()

    # holds terrain
    terrain_list = pygame.sprite.Group()
    ground = Ground(game, GREEN)
    terrain_list.add(ground)

    # holds everything that needs to be drawn
    draw_list = []
    draw_list.append(asteroid_list)
    draw_list.append(terrain_list)


    # everything is drawn to this surface
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
                asteroid_list.remove(asteroid)

        #updated_asteroid_state = generateAsteroid(game, asteroid_list)
        game, asteroid_list = generateAsteroid(game, asteroid_list)

        ### DRAWING ###
        screen.fill(BLACK)
        for sprite_group in draw_list:
            sprite_group.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        fpsclock.tick(TICK_RATE)

if __name__ == '__main__':
    main()
