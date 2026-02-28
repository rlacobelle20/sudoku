class Board:
    def __init__(self):
        self.board = [[] for _ in range(9)] # creates board with empty rows
        pass

    def random_board(self):
        import random

        for i in range(9):
            tmp_lst = [1,2,3,4,5,6,7,8,9]
            random.shuffle(tmp_lst)

        random.random_board(self.board)
        