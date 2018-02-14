import pygame, helper

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, posx, posy, size, speed, game, color):
        super().__init__()

        self.game = game

        self.posx = posx
        self.posy = posy
        self.size = size
        self.speed = speed
        self.mass = self.size / game.asteroid_size_range[1]


        #!!!! Is this the best way??? Figure out a good way to use altitude !!!!#
        self.altitude = helper.WINDOW_HEIGHT - posy
        self.velocity = 0
        self.acceleration = 0

        self.color = color
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    def update(self):
        self.altitude = helper.update_altitude(self.altitude, self.velocity, self.game.ground_level)
        self.velocity = helper.update_velocity(self.velocity, self.acceleration)
        self.acceleration = helper.update_acceleration(self.game.gravity, self.mass)
        self.posy = helper.WINDOW_HEIGHT - self.altitude
        self.rect.y = self.posy


class GameVariables:
    def __init__(self, playing):
        self.playing = playing
        self.max_asteroids = 0
        self.asteroid_size_range = []
        self.asteroid_speed_range = []
        self.gravity = 0
        self.ground_level = 0
