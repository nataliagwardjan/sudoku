import pytest
from sudoku import SudokuBoard, Sudoku


@pytest.mark.parametrize(
    "board, limit, expected_solutions_count, is_valid",
    [
        # Case 1: Board is correct and has only one solution
        (
                [
                    [5, 3, 4, 6, 0, 8, 9, 0, 0],
                    [6, 7, 2, 1, 0, 5, 3, 0, 8],
                    [1, 9, 8, 3, 4, 0, 5, 6, 7],
                    [8, 5, 9, 7, 0, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ],
                1,
                1,
                True,
        ),
        # Case 2: Board is correct and has 8 solutions
        (
                [
                    [0, 3, 0, 0, 0, 8, 0, 0, 0],
                    [0, 0, 0, 1, 0, 5, 0, 0, 0],
                    [1, 0, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 1, 4, 2, 0],
                    [4, 2, 0, 0, 0, 3, 7, 9, 1],
                    [0, 0, 3, 0, 2, 4, 0, 0, 0],
                    [0, 6, 1, 0, 3, 0, 2, 0, 4],
                    [0, 0, 0, 4, 0, 0, 6, 0, 0],
                    [0, 4, 0, 2, 8, 6, 0, 0, 0]
                ],
                0,
                8,
                True,
        ),
        # Case 3: Board is correct, has 2 solutions, we expect 5
        (
                [
                    [0, 3, 0, 0, 0, 8, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 3, 0, 8],
                    [1, 0, 8, 0, 0, 0, 0, 6, 7],
                    [8, 0, 0, 0, 6, 1, 4, 2, 3],
                    [4, 2, 6, 0, 5, 3, 7, 9, 1],
                    [0, 1, 3, 0, 2, 4, 0, 5, 6],
                    [0, 6, 1, 5, 3, 0, 2, 8, 4],
                    [0, 0, 0, 4, 1, 0, 6, 3, 0],
                    [0, 4, 5, 2, 8, 6, 1, 7, 0]
                ],
                5,
                2,
                True,
        ),
        # Case 4: Board is correct input but has no solutions
        (
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                ],
                0,
                0,
                False,
        ),
        # Case 5: Board is invalid
        (
                [
                    [5, 5, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9],
                ],
                0,
                0,
                False,
        ),
    ],
)
def test_sudoku(board, limit, expected_solutions_count, is_valid):
    sudoku_board = SudokuBoard(board)
    assert sudoku_board.is_valid() == is_valid

    if is_valid:
        sudoku = Sudoku(sudoku_board)
        sudoku.find_all_solutions(limit=limit)
        assert len(sudoku.solutions) == expected_solutions_count
