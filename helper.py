import random
from game_objects import *

### SYSTEM VARIABLES ###

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1080
TICK_RATE = 20
WORLD_SCALE = 5

### COLORS ###
BLACK = [0, 0, 0]
GRAY = [200, 200, 200]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]

### GAME FUNCTIONS ###

def altitudeToPixels(altitude):
    return WINDOW_HEIGHT - altitude

def generateAsteroid(game, asteroid_list):
    if game.asteroid_spawn_counter >= game.asteroid_spawn_cooldown:
        if len(asteroid_list) < game.max_asteroids:
            # generate an asteroid
            game.asteroid_spawn_counter = 0
            pos = genRandomPos(WINDOW_WIDTH, WINDOW_HEIGHT)
            pos_x = pos[0]
            altitude = pos[1]
            size = random.randint(game.asteroid_size_range[0], game.asteroid_size_range[1])
            color = genRandomGray()
            asteroid = Asteroid(pos_x, altitude, size, game, color)
            asteroid_list.add(asteroid)
    else:
        game.asteroid_spawn_counter += 1
    return game, asteroid_list

def genRandomPos(x_range, ceiling):
    #!!!! FIX LATER TO MAKE SURE ASTEROIDS STAY WITHIN BOUNDS !!!!#
    #!!!! FIX LATER TO ENSURE ASTEROIDS DON'T SPAWN WITHIN OTHER ASTEROIDS !!!!$
    rand_x = random.randint(x_range / 15, x_range - x_range / 15)
    return(rand_x, ceiling - 20)

def genRandomGray():
    val = random.randint(150, 255)
    return (val, val, val)

def update_altitude(altitude, velocity, ground_level):
    if altitude + velocity > ground_level:
        return altitude + velocity
    else:
        return ground_level

def update_velocity(velocity, acceleration, terminal_velocity):
    if abs(velocity + acceleration) <= abs(terminal_velocity):
        return velocity + acceleration
    else:
        return terminal_velocity

def update_acceleration(gravity, mass):
    return -(gravity * mass)
