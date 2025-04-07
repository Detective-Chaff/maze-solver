# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from tkinter import Canvas

class Line():
    def __init__(self, point1, point2):
        self._point_one = point1
        self._point_two = point2

    def draw(self, canvas, colour:str):
        canvas.create_line(
            self._point_one.x,
            self._point_one.y,
            self._point_two.x,
            self._point_two.y,
            fill=colour,
            width=2
        )