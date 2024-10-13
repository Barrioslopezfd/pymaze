from graphics import *
from maze import Maze

def main():
    win = Window(1000, 1000)
    maze = Maze(100, 100, 8, 8, 20, 20, win)
    maze.solve()
    win.wait_for_close()
main()
