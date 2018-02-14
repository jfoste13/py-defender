import pygame, helper

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, posx, altitude, size, game, color):
        super().__init__()

        self.game = game

        self.posx = posx
        self.altitude = altitude
        self.size = size
        self.mass = self.size / game.asteroid_size_range[1]

        self.ground_contact = False

        self.velocity = 0
        self.terminal_velocity = -10
        self.acceleration = 0

        self.color = color
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = posx
        #!!!!! FIGURE OUT WHY 80 WORKS !!!!!#
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.size

    def update(self):
        self.altitude = helper.update_altitude(self.altitude, self.velocity, self.game.ground_level)
        self.velocity = helper.update_velocity(self.velocity, self.acceleration, self.terminal_velocity)
        self.acceleration = helper.update_acceleration(self.game.gravity, self.mass)
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.size
        self.ground_contact = self.groundContact()

    def groundContact(self):
        if self.altitude == 0:
            return True
        else:
            return False


class GameVariables:
    def __init__(self, playing):
        self.playing = playing
        self.max_asteroids = 0
        self.asteroid_size_range = []
        self.asteroid_speed_range = []
        self.gravity = 0
        self.ground_level = 0
