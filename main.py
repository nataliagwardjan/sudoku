import sudoku


def get_sudoku_board_from_user():
    sudoku_board = []
    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 9:
            raise ValueError("Each row must contain exactly 9 numbers!")
        sudoku_board.append(row)

    limit: int = (int(input(f"What is your limit of solutions: ")))

    return sudoku.SudokuBoard(sudoku_board), limit


if __name__ == "__main__":

    board, limit = get_sudoku_board_from_user()
    sudoku_board = sudoku.SudokuBoard()

    if not sudoku_board.is_valid():
        raise ValueError("The Sudoku board is invalid!")

    sudoku = sudoku.Sudoku(sudoku_board)

    sudoku.find_all_solutions(limit=limit)

    sudoku.print_solutions()
