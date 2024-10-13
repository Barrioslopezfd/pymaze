from time import sleep

from cell import Cell
from graphics import Window


class Maze:
    def __init__(self,
                 x1: int,
                 y1: int,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 win: Window|None=None,
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []
        self.__create_cells()

    def __create_cells(self):
        if self.win == None:
            return

        for i in range(self.num_cols):
            cells_col = []
            for j in range(self.num_rows):
                cl = Cell(
                    self.x1+self.cell_size_x*i, 
                    self.y1+self.cell_size_y*j, 
                    self.x1+self.cell_size_x*(i+1), 
                    self.y1+self.cell_size_y*(j+1), 
                    self.win)
                cells_col.append(cl)
            self._cells.append(cells_col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)
        self.__break_entrance_and_exit()

    def __draw_cell(self, i: int, j: int):
        self._cells[i][j].draw()
        self.__animate()

    def __animate(self):
        if self.win == None:
            return
        self.win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        if self.win == None or self._cells == []:
            return

        self._cells[0][0].top = 0
        self.__draw_cell(0,0)
        self._cells[-1][-1].bottom = 0
        self.__draw_cell(-1,-1)
