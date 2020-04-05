from graph import *
from math import *

def brow(with_brow, height_brow, k, angle_brow, x_eye, y_eye, r_eye):
    '''рисует бровь как касательную к глазу'''
    # находим точку на окружности чараз которую проходит касательная с  задонным углом
    #
    alfa = radians(angle_brow)
    beta = radians(angle_brow - 180)
    xa = x_eye + r_eye * cos(alfa)  # координата точки на окруности
    ya = y_eye + r_eye * sin(alfa)

    x1 = xa + k * with_brow * sin(beta)
    y1 = ya + k * with_brow * cos(alfa)
    x2 = xa + (1 - k) * with_brow * sin(alfa)
    y2 = ya + (1 - k) * with_brow * cos(beta)

    xb = x_eye + (r_eye + height_brow) * cos(alfa)  # координата точки на окруности
    yb = y_eye + (r_eye + height_brow) * sin(alfa)

    x3 = xb + k * with_brow * sin(beta)
    y3 = yb + k * with_brow * cos(alfa)
    x4 = xb + (1 - k) * with_brow * sin(alfa)
    y4 = yb + (1 - k) * with_brow * cos(beta)
    polygon([(x1, y1), (x3, y3), (x4, y4), (x2, y2), (x1, y1), ])



with_w = 350
height_w = 350
windowSize(with_w, height_w)

center_x = height_w // 2
center_y = with_w // 2

penColor("black")
penSize(1)

# овал лица
R_faice = 150
brushColor("yellow")
circle(center_x, center_y, R_faice)

# рот
with_lips = 130
height_lips = 50
brushColor("black")
x_lips = center_x - with_lips // 2
y_lips = center_y + R_faice // 2 - height_lips // 2
rectangle(x_lips, y_lips, x_lips + with_lips, y_lips + height_lips)

r_eye_right = 20
r_pupil_right = 15
r_eye_left = 30
r_pupil_left = 10
with_eye = 50
height_eye = 70

# right eye
x_eye_right = center_x - with_eye
y_eye_right = center_y - height_eye // 2
penColor("red")
brushColor("red")
circle(x_eye_right, y_eye_right, r_eye_right)
# right eye pupil
brushColor("black")
circle(x_eye_right, y_eye_right, r_pupil_right)

# left eye
x_eye_left = center_x + with_eye
y_eye_left = center_y - height_eye // 2
penColor("red")
brushColor("red")
circle(x_eye_left, y_eye_left, r_eye_left)
# right eye pupil
penColor("white")
brushColor("white")
penSize(1)
circle(x_eye_left, y_eye_left, r_pupil_left)

penColor("black")
brushColor("black")
brow(80, 15, 0.3, 290, x_eye_right, y_eye_right, r_eye_right)
brow(80, 15, 0.7, 250, x_eye_left, y_eye_left, r_eye_left)

run()
