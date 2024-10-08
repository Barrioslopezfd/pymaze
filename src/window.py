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
    def close(self):
        self.wRunning = False

