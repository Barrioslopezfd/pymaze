import random
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
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_visited()

    def __create_cells(self):
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

    def __check_if_exists(self, i: int, j: int) -> Cell | None:
        if 0 <= i < len(self._cells) and 0 <= j < len(self._cells[0]):
            return self._cells[i][j]

    def __break_walls_r(self, i: int, j: int) -> None:
        current_cell = self._cells[i][j]
        current_cell.visited = True
        top=(i, j-1)
        bottom=(i, j+1)
        left=(i-1, j)
        right=(i+1, j)
        while True:
            to_visit=[]
            possible_directions=[]
            top_cell = self.__check_if_exists(top[0], top[1])
            bottom_cell = self.__check_if_exists(bottom[0], bottom[1])
            left_cell=self.__check_if_exists(left[0], left[1])
            right_cell=self.__check_if_exists(right[0], right[1])

            if top_cell != None and top_cell.visited == False:
                possible_directions.append((top[0], top[1]))
            if bottom_cell != None and bottom_cell.visited == False:
                possible_directions.append((bottom[0], bottom[1]))
            if left_cell != None and left_cell.visited == False:
                possible_directions.append((left[0], left[1]))
            if right_cell != None and right_cell.visited == False:
                possible_directions.append((right[0], right[1]))

            if possible_directions == []:
                self.__draw_cell(i, j)
                return
            to_visit = random.choice(possible_directions)
            if to_visit == top:
                current_cell.top=0
                self.__break_walls_r(to_visit[0], to_visit[1])
            elif to_visit == bottom:
                current_cell.bottom=0
                self.__break_walls_r(to_visit[0], to_visit[1])
            elif to_visit == left:
                current_cell.left=0
                self.__break_walls_r(to_visit[0], to_visit[1])
            elif to_visit == right:
                current_cell.right=0
                self.__break_walls_r(to_visit[0], to_visit[1])

    def __reset_visited(self) -> None:
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited=False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, x: int, y: int):
        current_cell = self._cells[x][y]
        self.__animate()
        current_cell.visited = True
        if x == self.num_cols-1 and y == self.num_rows-1:
            return True

        top=(x, y-1)
        bottom=(x, y+1)
        left=(x-1, y)
        right=(x+1, y)

        top_cell = (self.__check_if_exists(top[0], top[1]), current_cell.top, top)
        bottom_cell = (self.__check_if_exists(bottom[0], bottom[1]), current_cell.bottom, bottom)
        left_cell=(self.__check_if_exists(left[0], left[1]), current_cell.left, left)
        right_cell=(self.__check_if_exists(right[0], right[1]), current_cell.right, right)

        directions = (top_cell, bottom_cell, left_cell, right_cell)

        for dir in directions:
            if dir[0] != None and dir[1] == 0 and dir[0].visited == False:
                current_cell.draw_move(dir[0])
                solved = self._solve_r(dir[2][0], dir[2][1])
                if solved:
                    return solved
                else: 
                    current_cell.draw_move(dir[0], True)
        return False
