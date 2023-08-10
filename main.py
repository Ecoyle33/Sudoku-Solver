def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet ---> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind we're using zero-indexing (0-8) for the indices

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None   # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if valid, False otherwise

    # start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # sudoku square
    # want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we pass all these checks, the square's valid
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking instead of
    # how humans tend to solve sudoku puzzles

    # puzzle is a list of lists, each inner list is a row in the puzzle
    # return whether a solution exists
    # mutates the puzzle to be the solution (if the solution exists)

    # choose somewhere on the puzzle to make a guess
    # helper function that finds the open spaces in the puzzle
    row, col = find_next_empty(puzzle)

    # if there's nowhere left then we're done, we only allowed valid inputs
    if row is None:
        return True

    # if there is a place to put a number, then make a guess between 1 and 9

    for guess in range(1, 10):
        # check if this is a valid guess
        if is_valid(puzzle, guess, row, col):  # another helper function
            # if valid, place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            if solve_sudoku(puzzle):
                return True

        # if invalid or if our guess doesn't solve the puzzle, we need to
        # backtrack and try a new number
        puzzle[row][col] = -1  # reset the guess

    # if none of the numbers work, the puzzle is unsolvable

    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)