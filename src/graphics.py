from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.root=Tk()
        self.title = self.root
        self.canvas = Canvas()
        self.canvas.pack()
        self.wRunning=False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.update()
        self.canvas.update_idletasks()

    def wait_for_close(self):
        self.wRunning = True
        while self.wRunning == True:
            self.redraw()
        print("CLOSED")
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
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

