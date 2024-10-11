from graphics import Window
from cell import Cell
from time import sleep

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

        for i in range(self.num_cols+1):
            cells_col = []
            for j in range(self.num_rows+1):
                cl = Cell(self.x1+self.cell_size_x*i, self.y1+self.cell_size_y*j, self.x1+self.cell_size_x, self.y1+self.cell_size_y, self.win)
                cells_col.append(cl)
            self.__cells.append(cells_col)

        for i in range(self.num_cols+1):
            for j in range(self.num_rows+1):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        if self.win == None:
            return

        self.win.redraw()
        sleep(0.05)
