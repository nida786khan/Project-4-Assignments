""" Eraser on Canvas - By [Your Name] """

from graphics import Canvas
import time

CANVAS_SIZE, CELL_SIZE, ERASER_SIZE = 400, 40, 20

def erase(canvas, eraser):
    """ Jo bhi eraser touch kare, usko white kar do """
    x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
    for obj in canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE):
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    
    # 🟦 Grid create karo
    for r in range(0, CANVAS_SIZE, CELL_SIZE):
        for c in range(0, CANVAS_SIZE, CELL_SIZE):
            canvas.create_rectangle(c, r, c + CELL_SIZE, r + CELL_SIZE, 'blue')

    canvas.wait_for_click()
    x, y = canvas.get_last_click()
    eraser = canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, 'gray')

    while True:
        canvas.moveto(eraser, canvas.get_mouse_x(), canvas.get_mouse_y())
        erase(canvas, eraser)
        time.sleep(0.03)

if __name__ == '__main__':
    main()
