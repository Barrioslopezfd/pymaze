from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.root=Tk()
        self.root.title('Maze Solver')
        self.canvas = Canvas(self.root, bg='white', height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.wRunning=False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.update_idletasks()
        self.canvas.update()

    def wait_for_close(self):
        self.wRunning = True
        while self.wRunning == True:
            self.redraw()
        print("Window closed!")
    def close(self):
        self.wRunning = False

    def draw_line(self, line: 'Line', fill_color: str):
        line.draw(self.canvas, fill_color)

class Line:
    def __init__(self, pointA, pointB) -> None:
        self.x1 = pointA.x
        self.y1 = pointA.y
        self.x2 = pointB.x
        self.y2 = pointB.y

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
        )

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
class Cell:
    def __init__(self, top: bool, bottom: bool, left: bool, right: bool, x1: int, y1:int, x2: int, y2:int, win: Window) -> None:
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.left:
            pntA = Point(self.x1, self.y1)
            pntB = Point(self.x1, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.right:
            pntA = Point(self.x2, self.y1)
            pntB = Point(self.x2, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.top:
            pntA = Point(self.x1, self.y1)
            pntB = Point(self.x2, self.y1)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.bottom:
            pntA = Point(self.x1, self.y2)
            pntB = Point(self.x2, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
