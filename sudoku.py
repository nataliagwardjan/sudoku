class SudokuBoard:
    def __init__(self, board: list[list] = None):
        """
        Initializes the Sudoku board.
        If no board is provided, a 9x9 grid filled with zeros is created.
        """
        self.board = board if board else [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(self):
        """
        Checks the validity of the input data. Numbers must be in the range 0-9,
        and rows, columns, and blocks must not contain duplicates (except 0).
        """
        for row in self.board:
            if any(num < 0 or num > 9 for num in row):
                return False

        return (
                all(self._has_no_duplicates(self._get_row(i)) for i in range(9))
                and
                all(self._has_no_duplicates(self._get_col(i)) for i in range(9))
                and
                all(
                    self._has_no_duplicates(self._get_block(i, j))
                    for i in range(0, 9, 3)
                    for j in range(0, 9, 3)
                )
        )

    def _has_no_duplicates(self, nums):
        """
        Helper function to check if a list has no duplicates (excluding zeros).
        """
        nums = [num for num in nums if num != 0]
        return len(nums) == len(set(nums))

    def _get_row(self, row):
        """
        Returns the row at index `row`.
        """
        return self.board[row]

    def _get_col(self, col):
        """
        Returns the column at index `col`.
        """
        return [self.board[row][col] for row in range(9)]

    def _get_block(self, start_row, start_col):
        """
        Returns the 3x3 block starting at (start_row, start_col).
        """
        return [
            self.board[row][col]
            for row in range(start_row, start_row + 3)
            for col in range(start_col, start_col + 3)
        ]

    def print_board(self):
        """
        Displays the Sudoku board in a readable format with grid separators.
        """
        for i, row in enumerate(self.board):
            if i > 0 and i % 3 == 0:
                print("------+-------+------")
            print(" ".join(
                str(row[j]) if row[j] != 0 else "0"
                if (j + 1) % 3 else f"{row[j] if row[j] != 0 else '0'} |"
                for j in range(9)
            ).strip(" |"))


class Sudoku:
    def __init__(self, sudoku_board: SudokuBoard):
        """
        Initializes the Sudoku object with the initial SudokuBoard.
        """
        self.sudoku_board = sudoku_board
        self.solutions = set()

    def find_all_solutions(self, limit: int = 1):
        """
        Finds all possible solutions to the Sudoku board, up to the specified limit.
        If limit is 0, finds all solutions.
        """
        def backtrack(board):
            if limit and len(self.solutions) >= limit:
                return

            for row in range(9):
                for col in range(9):
                    if board.board[row][col] == 0:
                        for num in range(1, 10):
                            board_copy = SudokuBoard([row[:] for row in board.board])
                            board_copy.board[row][col] = num

                            if board_copy.is_valid():
                                backtrack(board_copy)
                        return

            solved_board = SudokuBoard([row[:] for row in board.board])
            self.solutions.add(self._board_to_tuple(solved_board.board))

        backtrack(self.sudoku_board)

    def _board_to_tuple(self, board):
        """
        Converts a 2D board into a tuple to make it hashable for storage in a set.
        """
        return tuple(tuple(row) for row in board)

    def print_solutions(self):
        """
        Displays all found solutions.
        """
        if not self.solutions:
            print("No solutions found.")
        else:
            print(f"Found {len(self.solutions)} solution(s):")
            for idx, solution in enumerate(self.solutions):
                print(f"\nSolution {idx + 1}:")
                for row in solution:
                    print(" ".join(str(num) for num in row))
