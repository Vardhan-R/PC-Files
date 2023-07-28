import manim, math, pygame, random, time
from built_modules import import_vectors as vect

pygame.init()

scrn_width = 1600
scrn_height = 1200
running = True
total_width = 8000
total_height = 6000
ang_a = 2 * math.atan(4)
ang_b = 2 * math.atan(3)
translate_spd = 1
zoom_spd = 0.1
prev_state = {"w": False, "a": False, "s": False, "d": False, "q": False, "e": False, "left_mouse_button": False}
all_circles = [vect.Vector(2030, 1570), vect.Vector(2200, 1627), vect.Vector(2400, 1983), vect.Vector(2500, 1707), vect.Vector(2700, 2057), vect.Vector(2350, 1870)]
all_rects = [vect.Vector(0, 0)]

scrn = pygame.display.set_mode((scrn_width, scrn_height))

class Cam:
    def __init__(self, pos_x: float | int, pos_y: float | int, pos_z: float | int):
        self.pos = vect.Vector(pos_x, pos_y, pos_z)
        self.initial_pos = self.pos
        self.state = False

    def translate(self, x: float | int, y: float | int, z: float | int = 0):
        self.pos = vect.add(self.pos, vect.Vector(x, y, z))

    def moveToMouse(self, mouse_moved: vect.Vector, remember_cam_pos: bool = False):
        if remember_cam_pos:
            self.initial_pos = self.pos
        else:
            self.pos = vect.sub(self.initial_pos, mouse_moved.mult(-2 * cam_1.pos.z * math.tan(ang_a / 2) / scrn_width))

cam_1 = Cam(2000, 1500, -500)
cam_1.state = True

while running:
    scrn.fill(manim.BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            present_key = pygame.key.name(event.key)
            if present_key == "w":
                cam_1.translate(0, -translate_spd)
                prev_state[present_key] = True
            if present_key == "a":
                cam_1.translate(-translate_spd, 0)
                prev_state[present_key] = True
            if present_key == "s":
                cam_1.translate(0, translate_spd)
                prev_state[present_key] = True
            if present_key == "d":
                cam_1.translate(translate_spd, 0)
                prev_state[present_key] = True
            if present_key == "q":
                cam_1.translate(0, 0, -zoom_spd)
                prev_state[present_key] = True
            if present_key == "e":
                cam_1.translate(0, 0, zoom_spd)
                cam_1.pos.z = min(cam_1.pos.z, -10)
                prev_state[present_key] = True

        if event.type == pygame.KEYUP:
            present_key = pygame.key.name(event.key)
            if present_key in ["w", "a", "s", "d", "q", "e"]:
                prev_state[present_key] = False

        if pygame.mouse.get_pressed()[0]:
            if not(prev_state["left_mouse_button"]):
                initial_mouse_x, initial_mouse_y = pygame.mouse.get_pos()
                prev_state["left_mouse_button"] = True
                cam_1.moveToMouse(vect.Vector(0, 0), True)
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cam_1.moveToMouse(vect.Vector(mouse_x - initial_mouse_x, mouse_y - initial_mouse_y))
        else:
            prev_state["left_mouse_button"] = False

    if prev_state["w"]:
        cam_1.translate(0, -translate_spd)
    if prev_state["a"]:
        cam_1.translate(-translate_spd, 0)
    if prev_state["s"]:
        cam_1.translate(0, translate_spd)
    if prev_state["d"]:
        cam_1.translate(translate_spd, 0)
    if prev_state["q"]:
        cam_1.translate(0, 0, -zoom_spd)
    if prev_state["e"]:
        cam_1.translate(0, 0, zoom_spd)
        cam_1.pos.z = min(cam_1.pos.z, -10)

    scale_factor = -scrn_width / (2 * cam_1.pos.z * math.tan(ang_a / 2))
    for i in all_rects:
        pygame.draw.rect(scrn, manim.WHITE, pygame.Rect(((i.x - cam_1.pos.x) * scale_factor) + scrn_width / 2, (i.y - cam_1.pos.y) * scale_factor + scrn_height / 2, total_width * scale_factor, total_height * scale_factor))
    for i in all_circles:
        pygame.draw.circle(scrn, manim.PURE_RED, ((i.x - cam_1.pos.x) * scale_factor + scrn_width / 2, (i.y - cam_1.pos.y) * scale_factor + scrn_height / 2), 50 * scale_factor)
    pygame.draw.circle(scrn, manim.PURE_BLUE, (scrn_width / 2, scrn_height / 2), 10 * scale_factor)

    zoom_spd = math.log(1 - cam_1.pos.z / 500)

    pygame.display.update()

pygame.quit()

# scale factor should be an attribute of cams