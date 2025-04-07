
class Point():
    def __init__(self, x, y):
        self._x = x # horizontal (0 is left of window)
        self._y = y # vertical (0 is top of window)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y