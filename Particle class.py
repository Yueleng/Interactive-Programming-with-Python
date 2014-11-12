# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1,0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:

    # initializer for particles
    def __init__(self, position, color):
        # two input parameters: position, color
        # parameter 'self' is for reference inside the class.
        self.position = position
        self.color = color

    # method that updates position of a particle
    def move(self, offset):
        # every movement by plus a vector called offset.
        self.position[0] += offset[0]
        self.position[1] += offset[1]

    # draw method for particles

    def draw(self, canvas):
        # canvas.draw_circle(center_point, radius, line_width, line_color, fill_color = color)
        canvas.draw_circle(self.position, PARTICLE_RADIUS, 1, self.color, self.color)

    # string method for particles
    # string method is for printing out.
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color


# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))

    for p in particle_list:
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(100):
    # initialize the Particle class in the lefthand side and assign it to the right handside.
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
    particle_list.append(p) # the list contain all the objects.

# start frame
frame.start()
