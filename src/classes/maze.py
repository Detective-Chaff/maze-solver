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
            ,cell_size_y
            ,win=None
            ,seed=None):
        self._x = x1
        self._y = y1
        self._num_rows = num_rows if num_rows > 0 else 1
        self._num_cols = num_cols if num_cols > 0 else 1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed:
            random.seed(seed)
        self._win = win
        self._cells = []

        self._create_cells()
        self._create_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
    
    '''
        _break_walls_r uses DFS traversal
    '''
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            #create new not visited neighbour list during each recursion call for the current cell
            not_visited = []
            
            # check for neighbouring cells
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Down, Right, Up, Left
                ni, nj = i + di, j + dj # Calculate new grid coordinates

                # Check bounds and visited status of neighbour cells using new grid coordinates
                if (0 <= ni and ni < len(self._cells)) and (0 <= nj and nj < len(self._cells[0])):
                    if not self._cells[ni][nj].visited:
                        not_visited.append((ni, nj)) # not visited neighbour positions in the maze grid

            # Break the loop if no unvisited neighbors
            if not not_visited:
                self._draw_cell(i,j)
                return

            direction_index = random.randrange(len(not_visited))
            next_cell = not_visited[direction_index]

            # knock walls out according to direction using 0 index for left and right neighbours and 1 index for top and bottom 
            # next cell is to the right of our current cell
            if next_cell[0] == i + 1:
                self._cells[i][j].right_wall = False
                self._cells[i + 1][j].left_wall = False
            
            # next cell is to the left of our current cell
            if next_cell[0] == i - 1:
                self._cells[i][j].left_wall = False
                self._cells[i - 1][j].right_wall = False
            
            # next cell is at the bottom of our current cell
            if next_cell[1] == j + 1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j + 1].top_wall = False
            
            # next cell is at the top of our current cell
            if next_cell[1] == j - 1:
                self._cells[i][j].top_wall = False
                self._cells[i][j - 1].bottom_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])
            

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
    
    def solve_DFS(self):
        self.solve_DFS_r(0,0)
    
    def solve_DFS_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            print("FINISHED!!!")
            return True

        # move left
        if (i > 0 and self._cells[i][j].left_wall is False and self._cells[i - 1][j].visited is False):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self.solve_DFS_r(i - 1, j):# move to new cell
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        #move right
        if (i < self._num_cols - 1 and self._cells[i][j].right_wall is False and self._cells[i + 1][j].visited is False):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self.solve_DFS_r(i + 1, j):# move to new cell
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        #move down
        if (j < self._num_rows - 1 and self._cells[i][j].bottom_wall is False and self._cells[i][j + 1].visited is False):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self.solve_DFS_r(i,j + 1):# move to new cell
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        # move up
        if (j > 0 and self._cells[i][j].top_wall is False and self._cells[i][j - 1].visited is False):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self.solve_DFS_r(i,j - 1):# move to new cell
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        return False

    # def solve_BFS(self):
    #     self.solve_BFS_r(0,0)

    # def solve_BFS_r(self, i, j):
    #     self._animate()
    #     self._cells[i][j].visited = True




