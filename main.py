from src.classes.cell import Cell
from src.classes.line import Line
from src.classes.point import Point
from src.classes.window import Window


def main():
    print("starting")
    win = Window(800, 600)
    point_a = Point(200, 150)
    point_b = Point(600, 450)
    cell_a = Cell(win)

    cell_a.left_wall = False
    cell_a.bottom_wall = False
    cell_a.draw(point_a.x, point_a.y, point_b.x, point_b.y)
    # line = Line(point_a, point_b)
    # win.draw_line(line, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()