class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if (
                self.board[i] == col
                or self.board[i] - i == col - row
                or self.board[i] + i == col + row
            ):
                return False
        return True

    def solve(self, method="backtracking"):
        if method == "backtracking":
            self.backtrack(0)
        elif method == "branch_and_bound":
            self.branch_and_bound(0)

    def backtrack(self, row):
        if row == self.n:
            self.solutions.append(list(self.board))
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.backtrack(row + 1)
                self.board[row] = -1

    def branch_and_bound(self, row):
        if row == self.n:
            self.solutions.append(list(self.board))
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.branch_and_bound(row + 1)
                self.board[row] = -1

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                line = ["Q" if col == row else "." for col in range(self.n)]
                print(" ".join(line))
            print()


# Example usage:
n = 4  # Change n to the desired board size
n_queens_backtracking = NQueens(n)
n_queens_branch_and_bound = NQueens(n)

print("Solutions using Backtracking:")
n_queens_backtracking.solve("backtracking")
n_queens_backtracking.print_solutions()

print("Solutions using Branch and Bound:")
n_queens_branch_and_bound.solve("branch_and_bound")
n_queens_branch_and_bound.print_solutions()