import pygame
from pygame.draw import *
from pygame.transform import *
import numpy as np
import random

YELLOW_PLEASANT = (252, 152, 49)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (65, 25, 0)
PINK = (243, 0, 191)
LIGHTBLUE_LAS_1 = (111, 205, 252)
LIGHTBLUE_LAS_2 = (4, 138, 205)
GREEN_BLACK = (4, 138, 1)
PINK_LIGHT = (254, 169, 163)
PINK_PLEASANT = (172, 67, 52)
BLACK_BLUE_PLEASANT = (48, 16, 38)
BROWN_BIRD = (66, 33, 11)
PINK_SKY = (255, 207, 171)
BLUE_SKY_PLEASANT = (179, 134, 148)
LIGHT_ORANGE = (255, 222, 176)
ANOTHER_LIGHT_ORANGE = (255, 196, 112)

pygame.init()


def layer_1(color, y_0_level, right_or_left):
    mountain_point = [[0, y_0_level - 50]]
    # the first mountain_point is drawing here (smooth)
    for i in range(10, 240):
        height_of_first_mountain_point = y_0_level * 0.7 - (i - 10) ** 2 / 400
        mountain_point.append([i, height_of_first_mountain_point])
    # there are i am drawing the next mountain_points
    x_cor_of_pick = []
    y_cor_of_pick = []
    x0 = 310
    y0 = y_0_level * 0.7
    for i in range(3):
        x0 += 60
        y0 += 15
        x_cor_of_pick.append(x0)
        y_cor_of_pick.append(y0)
        y0 -= 40
        x_cor_of_pick.append(x0)
        y_cor_of_pick.append(y0)
        x0 += 20

    for i in range(len(x_cor_of_pick)):
        mountain_point.append([x_cor_of_pick[i], y_cor_of_pick[i]])
    # i am drawing smooth mountain_point

    for i in range(680, 800):
        height_of_second_mountain_point = y_0_level * 0.7 + (i - 680) * (i - 700) * (i - 830) / 4000
        mountain_point.append([i, height_of_second_mountain_point])

    mountain_point.append([860, y_0_level * 0.7])
    # i am drawing smooth mountain_point
    for i in range(900, 970):
        height_of_third_mountain_point = y_0_level // 2 + (i - 900) ** 2 / 200
        mountain_point.append([i, height_of_third_mountain_point])

    mountain_point.append([1000, y_0_level * 0.5])
    if right_or_left == 'right':
        mountain_point.append([1050, y_0_level])
    else:
        mountain_point.append([1050, y_0_level - 80])

    polygon(screen, color, mountain_point)


def layer_2(color, y0_level, right_or_left):
    mountain_point = []

    first_list_points = [[0, y0_level], [0, y0_level - 70], [10, y0_level - 70]]
    for i in range(len(first_list_points)):
        mountain_point.append(first_list_points[i])
    # smooth line
    for i in range(35, 230):
        height_of_second_mountain = y0_level - 150 + (i - 35) * (i - 200) / 70
        mountain_point.append([i, height_of_second_mountain])
    x0 = 250
    y0 = y0_level - 150
    x_cor_of_pick = []
    y_cor_of_pick = []
    second_list_points = []
    for i in range(4):
        x0 += 30
        y0 += 70
        x_cor_of_pick.append(x0)
        y_cor_of_pick.append(y0)
        x0 += 30
        y0 -= 100
    for i in range(len(x_cor_of_pick)):
        point = [x_cor_of_pick[i], y_cor_of_pick[i]]
        second_list_points.append(point)
    # second_list_points = [[280, 370], [350, 420], [390, 320], [490, 350], [560, 420]]
    # not smooth
    for i in range(len(second_list_points)):
        mountain_point.append(second_list_points[i])
    # smooth line
    for i in range(650, 900):
        height_of_third_mountain = y0_level - 100 + 450 * ((650 / i) ** 12 - (650 / i) ** 6)
        mountain_point.append([i, height_of_third_mountain])

    mountain_point.append([900, y0_level - 200])
    mountain_point.append([1020, y0_level - 150])
    if right_or_left == 'left':
        mountain_point.append([1050, y0_level - 50])
    else:
        mountain_point.append([1050, y0_level + 50])
    polygon(screen, color, mountain_point)


def layer_3(color, y0_level, right_or_left):
    first_list_point = [[0, y0_level], [0, y0_level - 340], [150, y0_level - 400]]
    mountain_point = []
    for i in range(len(first_list_point)):
        mountain_point.append(first_list_point[i])
    # smooth line
    for i in range(250, 500):
        height_of_first_mountain = y0_level - 380 - (i - 250) * (i - 650) / 250
        mountain_point.append([i, height_of_first_mountain])
    # the second pick
    mountain_point.append([650, y0_level - 280])
    # smooth line
    for i in range(700, 1050):
        height_of_second_mountain = y0_level - 280 + (i - 700) * (i - 850) * (i - 1200) / 50000
        mountain_point.append([i, height_of_second_mountain])
    # the third pick
    mountain_point.append([1050, y0_level - 80])
    if right_or_left == 'right':
        mountain_point.append([1050, y0_level - 80])
    else:
        mountain_point.append([1050, y0_level + 80])

    polygon(screen, color, mountain_point)


def bird(x, y, size, color):
    size /= 50
    surf_under_bird = pygame.Surface([100 * size, 150 * size], pygame.SRCALPHA)
    brd = []
    for i in np.arange(0, 28 * size):
        a = 20 * size * ((np.tan((i / size - 6 * (np.pi) + 5) / 12) ** 2))
        brd.append([i, a])
    for i in np.arange(28 * size, 100 * size):
        a = size * (102 + i / size * (i / size - 50) / 100)
        brd.append([i, a])

    polygon(surf_under_bird, color, brd)
    screen.blit(rotate(surf_under_bird, 60), [x, y])


def draw_background(surface, color, size):
    rect(surface, color, size)


def draw_sun(surface, color, pos, radius):
    circle(surface, color, pos, radius)


FPS = 30
screen = pygame.display.set_mode((1050, 700))
screen.fill(PINK_LIGHT)

# background
draw_background(screen, PINK_LIGHT, (0, 0, 1050, 150))
draw_background(screen, LIGHT_ORANGE, (0, 150, 1050, 150))
draw_background(screen, ANOTHER_LIGHT_ORANGE, (0, 300, 1050, 150))
draw_background(screen, BLUE_SKY_PLEASANT, (0, 450, 1050, 150))

# sun
draw_sun(screen, YELLOW, (400, 100), 60)

# mountain_points
layer_1(YELLOW_PLEASANT, 300, 'right')
layer_2(PINK_PLEASANT, 450, 'left')
layer_3(BLACK_BLUE_PLEASANT, 780, 'left')

# birds
bird(200, 200, 20, BROWN_BIRD)
bird(400, 180, 20, BROWN_BIRD)
bird(500, 230, 20, BROWN_BIRD)
bird(420, 250, 20, BROWN_BIRD)

bird(750, 300, 40, BROWN_BIRD)
bird(800, 200, 20, BROWN_BIRD)
bird(670, 380, 20, BROWN_BIRD)
bird(610, 410, 25, BROWN_BIRD)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
