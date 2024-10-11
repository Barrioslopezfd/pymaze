from graphics import *

def main():
    win = Window(1000, 1000)
    Maze(100, 100, 8, 8, 100, 100, win)

    win.wait_for_close()
main()
