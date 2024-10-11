from tkinter import BOTH, Canvas, Tk
from time import sleep


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
    def __init__(self, x1: int, y1:int, x2: int, y2:int, win: Window, sides: tuple = (1,1,1,1)) -> None:
        self.top = sides[0]
        self.bottom = sides[1]
        self.left = sides[2]
        self.right = sides[3]
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.left == 1:
            pntA = Point(self.x1, self.y1)
            pntB = Point(self.x1, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.right == 1:
            pntA = Point(self.x2, self.y1)
            pntB = Point(self.x2, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.top == 1:
            pntA = Point(self.x1, self.y1)
            pntB = Point(self.x2, self.y1)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')
        if self.bottom == 1:
            pntA = Point(self.x1, self.y2)
            pntB = Point(self.x2, self.y2)
            ln = Line(pntA, pntB)
            self.win.draw_line(ln, 'black')

    def draw_move(self, to_cell: 'Cell', undo=False):
        clr = 'red'
        if undo:
            clr = 'gray'
        pntA = Point(self.x1+round((self.x2-self.x1)/2), self.y1+round((self.y2-self.y1)/2))
        pntB = Point(to_cell.x1+round((to_cell.x2-to_cell.x1)/2), to_cell.y1+round((to_cell.y2-to_cell.y1)/2))
        ln = Line(pntA, pntB)
        self.win.draw_line(ln, clr)

class Maze:
    def __init__(self,
                 x1: int,
                 y1: int,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 win: Window,
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells: list[list] = []
        self.__create_cells()

    def __create_cells(self):
        if self.win == None:
            return
        for i in range(self.num_cols):
            cells_col = []
            for j in range(self.num_rows):
                cl = Cell(self.x1+self.cell_size_x*i, self.y1+self.cell_size_y*j, self.x1+self.cell_size_x, self.y1+self.cell_size_y, self.win)
                cells_col.append(cl)
            self.__cells.append(cells_col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)
    def __draw_cell(self, i: int, j: int):
        self.__cells[i][j].draw()
        self.__animate()
    def __animate(self):
        if self.win == None:
            return
        self.win.redraw()
        sleep(0.05)
