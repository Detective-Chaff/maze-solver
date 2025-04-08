
import random
import time
from src.classes.cell import Cell


class Maze():
    def __init__(
            self
            ,x1
            ,y1
            ,num_rows
            ,num_cols
            ,cell_size_x
            ,cell_size_y,
            win=None):
        self._x = x1
        self._y = y1
        self._num_rows = num_rows if num_rows > 0 else 1
        self._num_cols = num_cols if num_cols > 0 else 1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._create_entrance_and_exit()
        print(f"{self._cells[self._num_cols - 1][self._num_rows - 1].bottom_wall}")
        print(f"{self._cells[self._num_cols - 1][self._num_rows - 1].right_wall}")

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
        
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self._x + i * self._cell_size_x
        y1 = self._y + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _create_entrance_and_exit(self):
        enter = random.randint(1,2)
        exit = random.randint(1,2)

        if enter == 1:
            self._cells[0][0].left_wall = False
            self._draw_cell(0,0)
        else:
            self._cells[0][0].top_wall = False
            self._draw_cell(0,0)
        
        if exit == 1:
            self._cells[self._num_cols - 1][self._num_rows - 1].right_wall = False
            self._draw_cell(self._num_cols - 1,self._num_rows - 1)
        else:
            self._cells[self._num_cols - 1][self._num_rows - 1].bottom_wall = False
            self._draw_cell(self._num_cols - 1,self._num_rows - 1)