"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """

        # current = (self._start_cell.row, self._start_cell.column)
        # current[0] -= 1
        # if self._valid_move(*current):
        #     self._mark_path(*current)
        # current[0] -= 1
        # if self._valid_move(*current):
        #     self._mark_path(*current)
        # else:
        #     current[0] += 1
        #     if self._valid_move(*current):
        #         self._mark_path(*current)

        current = (self._start_cell.row, self._start_cell.col)
        self._mark_path(*current)
        stack = Stack()
        stack.push(current)

        while not stack.is_empty() and not self._exit_found(*stack.peek()):
            current = stack.peek()
            # print(current)
            found = False

            for row, col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_cell = (current[0] + row, current[1] + col)
                if self._valid_move(*next_cell):
                    stack.push(next_cell)
                    self._mark_path(*next_cell)
                    found = True
                    break

            # for row in [-1, 1]:
            #     next = (current[0] + row, current[1])
            #     if self._valid_move(*next):
            #         stack.push(next)
            #         self._mark_path(*next)
            #         found = True
            #         break
            # if found:
            #     continue
            #
            # for col in [-1, 1]:
            #     next = (current[0], current[1] + col)
            #     if self._valid_move(*next):
            #         stack.push(next)
            #         self._mark_path(*next)
            #         found = True
            #         break

            if not found:
                self._mark_tried(*current)
                stack.pop()

        if stack.is_empty():
            return False
        elif self._exit_found(*stack.peek()):
            return True

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] in [Maze.PATH_TOKEN, Maze.TRIED_TOKEN]:
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        maze = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                maze += (self._maze_cells[row, col]
                         if self._maze_cells[row, col] is not None else "_") + " "
            maze += "\n"
        return maze

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col

# if __name__ == "__main__":
#     maze = Maze(4, 4)
