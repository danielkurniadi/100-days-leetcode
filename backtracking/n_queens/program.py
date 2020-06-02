
def solveNQueens(N):
    solutions = []
    board = []

    if N == 0: return [[]]

    def prettify_board(board):
        pretty = [["." for _ in range(N)]
                    for _ in range(N)]
        for col, row in board:
            pretty[row][col] = "Q"
        return ["".join(row) for row in pretty]

    def check_save(col, row, board):
        for col2, row2 in board:
            # check: same row
            if col == col2: return False
            # check: same col
            if row == row2: return False
            # check diagonal
            dy = abs(row2 - row)
            dx = abs(col2 - col)
            if dy == dx: return False
        return True

    def _recurse(row, board):
        if row == N:
            # stopping criterion
            solutions.append(board[:])
            return
        for col in range(N):
            if check_save(col, row, board):
                board.append((col, row))
                _recurse(row+1, board)
                board.pop()
        return

    _recurse(0, board)
    solutions = [prettify_board(board) for board in solutions]
    return solutions
