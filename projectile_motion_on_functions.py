from copy import deepcopy
from manim import *
import math, numpy as np, pygame, random, time

pygame.init()
random.seed(13)

width = 800
height = 600
running = True
r = 1
g = 0.05
initial_speed = 5

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

# def collision():
#     if pos.y + r > all_curve_pts[round(pos.x * c / width)].y:
#         if all_curve_pts[round(pos.x * c / width) - 1].y < all_curve_pts[round(pos.x * c / width) + 1].y:
#             vx += 1
#             pos.y = all_curve_pts[round(pos.x * c / width) + 1].y - r
#         elif all_curve_pts[round(pos.x * c / width) - 1].y > all_curve_pts[round(pos.x * c / width) + 1].y:
#             vx -= 1
#             pos.y = all_curve_pts[round(pos.x * c / width) - 1].y - r
#         else:
#             pos.y = all_curve_pts[round(pos.x * c / width)].y - r

def connect(surface, clr, ctrl_pts_lst, close=False):
    for m in range(len(ctrl_pts_lst) - 1): pygame.draw.line(surface, clr, (ctrl_pts_lst[m].x, ctrl_pts_lst[m].y), (ctrl_pts_lst[m + 1].x, ctrl_pts_lst[m + 1].y))
    if close: pygame.draw.line(surface, clr, (ctrl_pts_lst[-1].x, ctrl_pts_lst[-1].y), (ctrl_pts_lst[0].x, ctrl_pts_lst[0].y))

def pointOnCurve(points: list[Vector], t: int) -> Vector:
    new_pts_lst = []
    for i in range(len(points) - 1):
        new_pts_lst.append(Vector(t * points[i + 1].x + (1 - t) * points[i].x, t * points[i + 1].y + (1 - t) * points[i].y))
    if len(new_pts_lst) == 1:
        return new_pts_lst[0]
    else:
        return pointOnCurve(new_pts_lst.copy(), t)

ctrl_pts_lst = []
all_curve_pts = []
c = 1800
ctrl_pts = 8

# generating the control points of the Bézier curve
# for i in range(ctrl_pts):
#     ctrl_pts_lst.append(Vector(i * width / (ctrl_pts - 1), random.randint(height / 3, height)))
ctrl_pts_lst = [Vector(0, 475), Vector(170, 538), Vector(200, 558), Vector(285, 150), Vector(260, 153), Vector(275, 563), Vector(600, 565), Vector(800, 465)]

# generating the points of the terrain (Bézier curve)
all_curve_pts.append(pointOnCurve(ctrl_pts_lst, i / c))
for i in range(1, c + 1):
    temp = pointOnCurve(ctrl_pts_lst, i / c)
    if round(temp.x) != round(all_curve_pts[-1].x):
        all_curve_pts.append(temp)

scrn = pygame.display.set_mode((width, height))
scrn.fill(BLUE)
for i in range(len(all_curve_pts)):
    pygame.draw.line(scrn, GREEN_D, (all_curve_pts[i].x, height), (all_curve_pts[i].x, all_curve_pts[i].y))

all_x_disps = []
all_disp_sqs = []
all_dot_prods = []

# for i in range(10):
#     print(all_curve_pts[i].x)

for ang in range(49, 52):
    tm = 0
    launch_angle = -ang * DEGREES
    initial_vel = Vector(initial_speed * math.cos(launch_angle), initial_speed * math.sin(launch_angle))
    pos = deepcopy(all_curve_pts[5])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # collision()

        if pos.y <= all_curve_pts[round(pos.x)].y:
            pos.x = deepcopy(all_curve_pts[5]).x + initial_vel.x * tm
            pos.y = deepcopy(all_curve_pts[5]).y + initial_vel.y * tm + g * tm ** 2 / 2
        else:
            all_x_disps.append(pos.x - deepcopy(all_curve_pts[5]).x)
            all_disp_sqs.append((pos.x - deepcopy(all_curve_pts[5]).x) ** 2 + (pos.y - deepcopy(all_curve_pts[5]).y) ** 2)
            all_dot_prods.append(initial_vel.x ** 2 + initial_vel.y * (initial_vel.y + g * tm)) # initial_vel dot final_vel
            break

        # connect(scrn, PURE_BLUE, ctrl_pts_lst)
        pygame.draw.circle(scrn, (2 * ang + 75, 0, 0), (pos.x, pos.y), r)
        # connect(scrn, PURE_GREEN, all_curve_pts)

        tm += 0.1

        pygame.display.update()

for i in range(len(all_x_disps)):
    print(5 * i, all_x_disps[i], all_disp_sqs[i], all_dot_prods[i])

# pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()