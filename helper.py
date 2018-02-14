import random
from game_objects import *

### SYSTEM VARIABLES ###

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 720
TICK_RATE = 15
WORLD_SCALE = 5

### COLORS ###
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]

### GAME FUNCTIONS ###

def altitudeToPixels(altitude):
    return WINDOW_HEIGHT - altitude

def populateAsteroids(game, asteroid_list):
    while len(asteroid_list) < game.max_asteroids:
        # generate some asteroids
        pos = genRandomPos(WINDOW_WIDTH, WINDOW_HEIGHT)
        pos_x = pos[0]
        altitude = pos[1]
        size = random.randint(game.asteroid_size_range[0], game.asteroid_size_range[1])
        color = genRandomGray()
        asteroid = Asteroid(pos_x, altitude, size, game, color)
        asteroid_list.add(asteroid)
    return asteroid_list

def genRandomPos(x_range, y_range):
    #!!!! FIX LATER TO MAKE SURE ASTEROIDS STAY WITHIN BOUNDS !!!!#
    #!!!! FIX LATER TO ENSURE ASTEROIDS DON'T SPAWN WITHIN OTHER ASTEROIDS !!!!$
    rand_x = random.randint(1, x_range)
    altitude = random.randint(int(y_range *.8), y_range)
    return(rand_x, altitude)

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
