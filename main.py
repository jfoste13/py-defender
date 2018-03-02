import pygame, sys
from pygame.locals import *
from helper import *
from game_objects import *

def main():

    pygame.init()

    # handles all gameplay related variables
    game = GameVariables(True)
    game.max_asteroids = 40
    game.asteroid_size_range = [5, 20]
    game.gravity = .03
    game.ground_level = 10
    game.asteroid_spawn_cooldown = 30
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

    # holds projectiles
    projectile_list = pygame.sprite.Group()


    # holds everything that needs to be drawn
    draw_list = []
    draw_list.append(player_list)
    draw_list.append(asteroid_list)
    draw_list.append(terrain_list)
    draw_list.append(projectile_list)


    # everything is drawn to this surface
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # handles framerate
    fpsclock = pygame.time.Clock()

    ### MAIN GAME LOOP ###
    while game.playing:


        print(player_turret_arm.slope)

        ### INPUT ###
        #!!!!! MAKE MORE FLUID LATER !!!!!#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    player_turret_arm.rate = -.05
                elif event.key == K_d:
                    player_turret_arm.rate = .05
                elif event.key == K_s:
                    laser = LaserBullet(game, player_turret_arm.endpoint[0], altitudeToPixels(player_turret_arm.endpoint[1]), player_turret_arm.slope)
                    projectile_list.add(laser)
            elif event.type == pygame.KEYUP:
                if event.key == K_a or event.key == K_d:
                    player_turret_arm.rate = 0


        ### LOGIC ###
        player_turret_arm.update_arm_pos()
        player_turret_arm.update_angle()
        player_turret_arm.update_slope()
        for projectile in projectile_list:
            projectile.update()
        for asteroid in asteroid_list:
            for projectile in projectile_list:
                if pygame.sprite.collide_rect(asteroid, projectile):
                    asteroid.laser_contact = True
                    projectile_list.remove(projectile)
            asteroid.update()
            if asteroid.ground_contact or asteroid.destroyed:
                asteroid_list.remove(asteroid)
            if asteroid.laser_contact:
                asteroid.size -= 20
                asteroid.laser_contact = False

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
