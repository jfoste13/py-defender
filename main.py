import pygame, sys
from pygame.locals import *
from helper import *
from game_objects import *

def main():

    pygame.init()

    # handles all gameplay related variables
    game = GameVariables(True)
    game.max_asteroids = 10
    game.asteroid_size_range = [20, 50]
    game.gravity = .025
    game.ground_level = 10
    game.asteroid_spawn_cooldown = 60
    game.asteroid_spawn_counter = 0

    # holds a bunch of asteroids
    asteroid_list = pygame.sprite.Group()

    # holds terrain
    terrain_list = pygame.sprite.Group()
    ground = Ground(game, GREEN)
    terrain_list.add(ground)

    # holds player parts
    player_list = pygame.sprite.Group()
    player_base_main = PlayerBase(WINDOW_WIDTH / 2 - 50, 0, 100, 50, GRAY, game)
    player_turret_main = PlayerTurret(WINDOW_WIDTH / 2 - 25, 25, 50, 50, WHITE, game)
    player_turret_arm = PlayerTurretArm(player_turret_main, 100, 0, game)
    player_list.add(player_turret_main)
    player_list.add(player_base_main)

    # holds everything that needs to be drawn
    draw_list = []
    draw_list.append(player_list)
    draw_list.append(asteroid_list)
    draw_list.append(terrain_list)


    # everything is drawn to this surface
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # handles framerate
    fpsclock = pygame.time.Clock()

    ### MAIN GAME LOOP ###
    while game.playing:


        print(player_turret_arm.angle)

        ### INPUT ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    player_turret_arm.rate = -.05
                elif event.key == K_d:
                    player_turret_arm.rate = .05
            elif event.type == pygame.KEYUP:
                if event.key == K_a or event.key == K_d:
                    player_turret_arm.rate = 0


        ### LOGIC ###
        player_turret_arm.update_arm_pos()
        player_turret_arm.update_angle()
        for asteroid in asteroid_list:
            asteroid.update()
            if asteroid.ground_contact:
                asteroid_list.remove(asteroid)

        game, asteroid_list = generateAsteroid(game, asteroid_list)

        ### DRAWING ###
        screen.fill(BLACK)

        # draw turret arm
        pygame.draw.line(screen, RED, player_turret_arm.basepoint, player_turret_arm.endpoint)
        for sprite_group in draw_list:
            sprite_group.draw(screen)


        pygame.display.flip()
        pygame.display.update()
        fpsclock.tick(TICK_RATE)

if __name__ == '__main__':
    main()
