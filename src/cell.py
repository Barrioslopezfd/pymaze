from graphics import Line, Point, Window


class Cell:
    def __init__(self, x1: int, y1:int, x2: int, y2:int, win: Window|None = None, sides: tuple = (1,1,1,1)) -> None:
        self.top = sides[0]
        self.bottom = sides[1]
        self.left = sides[2]
        self.right = sides[3]
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        self.visited = False

    def draw(self):
        if self.win == None:
            return

        top_side = Line(Point(self.x1, self.y1),
                        Point(self.x2, self.y1))
        bottom_side = Line(Point(self.x1, self.y2),
                           Point(self.x2, self.y2))
        left_side = Line(Point(self.x1, self.y1), 
                         Point(self.x1, self.y2))
        right_side = Line(Point(self.x2, self.y1),
                          Point(self.x2, self.y2))
        if self.top == 1:
            self.win.draw_line(top_side, 'black')
        else:
            self.win.draw_line(top_side, 'white')

        if self.bottom == 1:
            self.win.draw_line(bottom_side, 'black')
        else:
            self.win.draw_line(bottom_side, 'white')

        if self.left == 1:
            self.win.draw_line(left_side, 'black')
        else:
            self.win.draw_line(left_side, 'white')

        if self.right == 1:
            self.win.draw_line(right_side, 'black')
        else:
            self.win.draw_line(right_side, 'white')

    def draw_move(self, to_cell: 'Cell', undo=False):
        if self.win == None:
            return
        clr = 'red'
        if undo:
            clr = 'gray'
        pntA = Point(self.x1+round((self.x2-self.x1)/2), self.y1+round((self.y2-self.y1)/2))
        pntB = Point(to_cell.x1+round((to_cell.x2-to_cell.x1)/2), to_cell.y1+round((to_cell.y2-to_cell.y1)/2))
        ln = Line(pntA, pntB)
        self.win.draw_line(ln, clr)

