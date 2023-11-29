from copy import deepcopy
import Backtracking


class SudokuModel:
    def __init__(self, board):
        self.orig_board = board
        self.curr_board = deepcopy(board)
        self.cand_board = None

    def ResetBoard(self):
        self.curr_board = deepcopy(self.orig_board)
        self.cand_board = None

    def GetBoard(self):
        return self.curr_board

    def GetAllCands(self):
        return self.cand_board

    def GetCell(self, i, j):
        return self.curr_board[i][j]

    def GetCands(self, i, j):
        return self.cand_board[i][j]

    def SetCell(self, i, j, value):
        self.curr_board[i][j] = value

    def Solve(self):
        Backtracking.BacktrackingAlgo(self.curr_board)
        self.GetBoard()
