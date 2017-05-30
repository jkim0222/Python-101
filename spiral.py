import time
import math
from graphics import *

_x1 = -400
_y1 = -300
_x2 = 400
_y2 = 300

def line(win, x1, y1, x2, y2, color):
    l = Line(Point(x1, y1), Point(x2, y2))
    l.setFill(color)
    l.draw(win)

def clearscreen(win):
    r = Rectangle(Point(_x1, _y1), Point(_x2, _y2))
    r.setFill("white")
    r.setOutline("white")
    r.draw(win)
    line(win, _x1, 0, _x2, 0, "black")
    line(win, 0, _y1, 0, _y2, "black")

def rec_spiral(win, ox, oy, base, color):
    x = 0
    y = 0
    for i in range(20):
        j = i % 4
        k = (i // 4) * 2
        dx = 0
        dy = 0
        if j == 0:
            dx = base * (k + 1)
        elif j == 1:
            dy = base * (k + 1)
        elif j == 2:
            dx = -base * (k + 2)
        else:
            dy = -base * (k + 2)
        line(win, ox + x, oy + y, ox + x + dx, oy + y + dy, color)
        time.sleep(0.05)
        x += dx
        y += dy

def dia_spiral(win, ox, oy, base, color):
    x = 0
    y = 0
    for i in range(20):
        j = i % 4
        k = (i // 4) * 2
        if j == 0:
            dx = base * (k + 1)
            dy = base * (k + 1)
        elif j == 1:
            dx = -base * (k + 1)
            dy = base * (k + 1)
        elif j == 2:
            dx = -base * (k + 2)
            dy = -base * (k + 2)
        else:
            dx = base * (k + 2)
            dy = -base * (k + 2)
        line(win, ox + x, oy + y, ox + x + dx, oy + y + dy, color)
        time.sleep(0.05)
        x += dx
        y += dy

def tri_spiral(win, ox, oy, n, base, color):

    for i in range(n):
        ang = (2 * math.pi / n) * i
        x = math.cos(ang) * 300
        y = math.sin(ang) * 300
        line(win, ox, oy, ox + x, oy + y, color)

    x = base
    y = 0
    for i in range(1, 30):
        ang = (2 * math.pi / n) * i
        r = base * (10.0 + i) / 10.0
        nx = math.cos(ang) * r
        ny = math.sin(ang) * r
        line(win, ox + x, oy + y, ox + nx, oy + ny, color)
        time.sleep(0.05)
        x = nx
        y = ny

def main():
    win = GraphWin("Spiral", _x2 - _x1 + 1, _y2 - _y1 + 1)
    win.setCoords(_x1, _y1, _x2, _y2)
    sp = 1          # rec_spiral
    base = 5
    color = "black"
    while True:
        clearscreen(win)
        if sp == 1:
            rec_spiral(win, 0, 0, base, color)
        elif sp == 2:
            dia_spiral(win, 0, 0, base, color)
        elif sp == 3:
            tri_spiral(win, 0, 0, 6, base, color)
        elif sp == 4:
            tri_spiral(win, 0, 0, 12, base, color)
        key = win.getKey()
        if key == 'q':
            break
        elif key == '1':
            sp = 1
        elif key == '2':
            sp = 2
        elif key == '3':
            sp = 3
        elif key == '4':
            sp = 4
        elif key == 'p':
            if base < 40:
                base += 5
        elif key == 'm':
            if base > 5:
                base -= 5
    win.close()  # Close window when done

main()