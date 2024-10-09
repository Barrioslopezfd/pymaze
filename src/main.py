from graphics import *

def main():
    win = Window(800, 600)
    pntA = Point(700, 100)
    pntB = Point(300, 300)
    ln = Line(pntA, pntB)
    win.draw_line(ln, 'black')
    win.wait_for_close()
main()
