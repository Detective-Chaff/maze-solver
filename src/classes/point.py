
class Point():
    def __init__(self, x, y):
        self._x = x # left of screen
        self._y = y # right of screen

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y