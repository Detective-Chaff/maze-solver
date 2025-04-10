from tkinter import Tk, BOTH, Canvas
from src.classes import line

'''
    Main class for creating a GUI window
'''
class Window():
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    '''
        Redraw is responsible for updating changes to the UI when called
        unlike reactive frameworks like React, Vue, or Angular 
        Tkinter does not automatically handle ui updates after changes
    '''
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line:line, colour="black"):
        line.draw(self.__canvas, colour)
