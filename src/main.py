from graphics import *

def main():
    win = Window(1000, 1000)
    cl1 = Cell(True, False, False, True, 100, 100, 200, 200, win)
    cl2 = Cell(True, False, True, False, 200, 100, 300, 200, win)
    cl3 = Cell(False, True, True, False, 100, 200, 200, 300, win)
    cl4 = Cell(False, True, False, True, 200, 200, 300, 300, win)

    cl1.draw()
    cl2.draw()
    cl3.draw()
    cl4.draw()

    win.wait_for_close()
main()
