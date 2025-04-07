from src.classes.cell import Cell
from src.classes.window import Window


def main():
    print("starting")
    win = Window(800, 600)
    #left
    c = Cell(win)
    # c.left_wall = False
    c.draw(50, 50, 100, 100)
    a = c
    #center left
    c = Cell(win)
    # c.right_wall = False
    c.draw(50, 100, 100, 150)
    #center right
    c = Cell(win)
    # c.bottom_wall = False
    c.draw(100, 50, 150, 100)
    b = c
    #right
    c = Cell(win)
    # c.top_wall = False
    c.draw(100, 100, 150, 150)
    a.draw_move(b)

    win.wait_for_close()

if __name__ == "__main__":
    main()