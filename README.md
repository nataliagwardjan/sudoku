# Sudoku Solver

This is a Python-based Sudoku solver that implements a backtracking algorithm to solve Sudoku puzzles. The `SudokuBoard` class represents the Sudoku board, and the `Sudoku` class handles the solving process and finding all possible solutions.

## Features

- Initialize a Sudoku board
- Validate Sudoku board (check if the current board configuration is valid)
- Print the Sudoku board in a readable format
- Find all possible solutions for a given board up to a specified limit
- Convert board to a tuple for hashing and storing in a set to handle multiple solutions

## Installation

To run the program, you need to have Python 3.12.0 or later installed on your machine. You can install the required dependencies using `pip` and the `requirements.txt` file.

1. Clone the repository or download the files.
2. Create a virtual environment and activate it.

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies using `pip`:
   Install the dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. Alternatively, you can install dependencies individually:
   ```bash
   pip install iniconfig==2.0.0
   pip install packaging==24.2
   pip install pluggy==1.5.0
   pip install pytest==8.3.3
   ```

## Dependencies

The following dependencies are required for the program to work:

- `iniconfig==2.0.0`
- `packaging==24.2`
- `pluggy==1.5.0`
- `pytest==8.3.3`

You can also check the exact installed versions with:
```bash
pip freeze
```

## Python Version

The program is compatible with Python 3.12.0 or later. You can check your Python version by running:
```bash
python --version
```

## Usage

After installing the dependencies, you can run the Sudoku solver program:

1. Create a `SudokuBoard` instance, optionally passing a 9x9 list of numbers to initialize the board.
2. Create a `Sudoku` instance with the `SudokuBoard` instance.
3. Call the `find_all_solutions()` method on the `Sudoku` instance to find solutions.

### Example

```python
from sudoku import SudokuBoard, Sudoku

# Initialize a Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create SudokuBoard instance
sudoku_board = SudokuBoard(board)

# Create Sudoku instance
sudoku = Sudoku(sudoku_board)

# Find all solutions (limit to 1 solution)
sudoku.find_all_solutions(limit=1)

# Print the solutions
sudoku.print_solutions()
```

### Sample Output

```
Found 1 solution(s):

Solution 1:
5 3 4 6 7 8 9 2 1
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9

```

## Running Tests

To run the tests, you can use `pytest`. The tests will ensure the validity of the Sudoku solver and board operations.

To run the tests:
```bash
pytest test_sudoku.py
```
