"""N Queens Problem."""


class NQueens(object):
    def __init__(self, size):
        super(NQueens, self).__init__()
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, current_row):
        if current_row == self.size:
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_position(positions, current_row, column):
                    positions[current_row] = column
                    self.put_queen(positions, current_row + 1)

    def check_position(self, positions, current_row, column):
        for row in range(current_row):
            if (
                positions[row] == column
                or positions[row] - row == column - current_row
                or positions[row] + row == column + current_row
            ):
                return False
        else:
            return True
