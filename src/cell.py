from graphics import Line, Point, Window


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

