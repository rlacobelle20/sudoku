class Sudoku:
    def __init__(self):
        # generate nine 1-9 lists where each number is in each spot once
        self.puzzle = []
        self.board = [["_" for _ in range(9)] for _ in range(9)] # creates empty list 9x9 -- _ reps no number
        pass
