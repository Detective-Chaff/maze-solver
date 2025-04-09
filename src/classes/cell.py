from src.classes.point import Point
from src.classes.line import Line


class Cell():

    def __init__(self, window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if  self.top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
            
    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "gray"

        center_y = (self._y1 + self._y2) // 2
        center_x = (self._x1 + self._x2) // 2
        p1 = Point(center_x, center_y)
            
        center_y = (to_cell._y1 + to_cell._y2) // 2
        center_x = (to_cell._x1 + to_cell._x2) // 2
        p2 = Point(center_x, center_y)
            
        cl = Line(p1,p2)
        self._win.draw_line(cl, colour)