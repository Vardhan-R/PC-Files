from built_modules import import_vectors as vect
import manim, pygame

pygame.init()

width = 1200
height = 1200
running = True
dt = 0.01
k = 0.1  # spring constant
l_0 = 200 # natural length of spring
m = 1     # mass of block
r_0 = 300 # initial radius

centre = vect.Vector(width / 2, height / 2)
pos = vect.Vector(width / 2, height / 2 - r_0) # position of block
vel = vect.Vector(2, 0)                        # velocity of block
acc = vect.Vector(0, 0)                        # acceleration of block

def calcdv():
    # a_c = (v_ perp) ** 2 / r
    # a_spring = -k * (r - l_0) / m

    r = vect.sub(pos, centre)                           # position of block w.r.t. the centre of the scrn

    v_parallel = r.setMag(vect.dot(vel, r.normalise())) # component of block's vel which is || to vector "r"
    v_perp = vect.sub(vel, v_parallel)                  # component of block's vel which is perpendicular to vector "r"

    a_c = r.setMag(v_perp.magSq() / r.mag())            # centrifugal acceleration
    a_spring = r.setMag(-k * (r.mag() - l_0) / m)       # acceleration due to spring

    global c
    if not(c % 1000):
        print(v_perp.mag())
        c = 0

    return vect.add(a_c, a_spring).mult(dt)             # magnitude is a_net * dt

def updatePos():
    global pos
    pos = vect.add(pos, vel.mult(dt))

def updateVel():
    global vel
    vel = vect.add(vel, calcdv())

scrn = pygame.display.set_mode((width, height))
scrn.fill(manim.BLACK)
pygame.draw.circle(scrn, manim.GREEN, (centre.x, centre.y), 5) # block (drawn as a circle)

c = 0
while running:
    # scrn.fill(manim.BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateVel()
    updatePos()

    # pygame.draw.line(scrn, manim.GREEN, (centre.x, centre.y), (pos.x, pos.y)) # spring
    pygame.draw.circle(scrn, manim.RED, (pos.x, pos.y), 2) # block (drawn as a circle)

    pygame.display.update()
    c += 1

pygame.quit()