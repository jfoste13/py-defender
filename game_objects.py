import pygame, helper, math


class LaserBullet(pygame.sprite.Sprite):
    def __init__(self, game, posx, altitude, slope):
        super().__init__()
        self.game = game
        self.posx = posx
        self.altitude = altitude
        self.slope = [int(slope[0] / 10), int(slope[1] / 10)]
        self.image = pygame.Surface([2, 2])
        self.image.fill(helper.RED)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = helper.altitudeToPixels(self.altitude)
    def update(self):
        self.altitude = self.altitude + self.slope[0]
        self.rect.x += self.slope[1]
        self.rect.y = helper.altitudeToPixels(self.altitude)
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, color):
        super().__init__()
        self.game = game
        self.color = color
        self.image = pygame.Surface([helper.WINDOW_WIDTH, self.game.ground_level])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = helper.altitudeToPixels(self.game.ground_level)

class PlayerBase(pygame.sprite.Sprite):
    def __init__(self, posx, altitude, width, height, color, game):
        super().__init__()
        self.game = game
        self.posx = posx
        self.altitude = altitude
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.height
class PlayerTurret(pygame.sprite.Sprite):
    def __init__(self, posx, altitude, width, height, color, game):
        super().__init__()
        self.game = game
        self.posx = posx
        self.altitude = altitude
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        pygame.draw.circle(self.image, self.color, [int(width / 2), int(height / 2)], int(width / 2))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.height
class PlayerTurretArm(pygame.sprite.Sprite):
    def __init__(self, turret, length, angle, game):
        self.game = game
        self.turret = turret
        self.angle = angle
        self.length = length
        self.basex = self.turret.posx + self.turret.width / 2
        self.basey = helper.altitudeToPixels(self.turret.altitude) - self.turret.height / 2
        self.basepoint = (self.basex, self.basey)
        self.endx = self.basex + math.cos(self.angle) * self.length
        self.endy = self.basey + math.sin(self.angle) * self.length
        self.endpoint = (self.endx, self.endy)
        self.rate = 0
        self.rise = -(self.endy - self.basey)
        self.run = self.endx - self.basex
        self.slope = [self.rise, self.run]
    def update_arm_pos(self):
        self.endx = self.basex + math.cos(self.angle) * self.length
        self.endy = self.basey + math.sin(self.angle) * self.length
        self.endpoint = (self.endx, self.endy)
    def update_angle(self):
        self.angle += self.rate
    def update_slope(self):
        self.rise = -(self.endy - self.basey)
        self.run = self.endx - self.basex
        self.slope = [self.rise, self.run]


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, posx, altitude, size, game, color):
        super().__init__()
        self.game = game
        self.posx = posx
        self.altitude = altitude
        self.size = size
        self.mass = self.size / game.asteroid_size_range[1]
        self.ground_contact = False
        self.laser_contact = False
        self.destroyed = False
        self.velocity = 0
        self.terminal_velocity = -1 * (size / 32)
        self.acceleration = 0
        self.color = color
        self.image = pygame.Surface([size, size])
        pygame.draw.circle(self.image, self.color, [int(self.size/2), int(self.size/2)], int(self.size/2))
        self.rect = self.image.get_rect()
        self.posx = posx
        self.rect.x = posx
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.size

    def update(self):
        if self.size <= 0:
            self.destroyed = True
            self.size = .0001

        self.image = pygame.Surface([self.size, self.size])
        pygame.draw.circle(self.image, self.color, [self.posx, int(self.size/2)], int(self.size/2))
        self.rect = self.image.get_rect()
        self.altitude = helper.update_altitude(self.altitude, self.velocity, self.game.ground_level)
        self.velocity = helper.update_velocity(self.velocity, self.acceleration, self.terminal_velocity)
        self.acceleration = helper.update_acceleration(self.game.gravity, self.mass)
        self.rect.y = helper.altitudeToPixels(self.altitude) - self.size
        self.ground_contact = self.groundContact()

    def groundContact(self):
        if self.altitude == self.game.ground_level:
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
        self.asteroid_spawn_cooldown = 0
        self.asteroid_spawn_Counter = 0
