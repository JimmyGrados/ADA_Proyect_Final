class BacktrackingAlgo:
    def __init__(self, board):
        self.board = board

    def solve(self, bo):
        find = self.find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(bo, i, (row, col)):
                bo[row][col] = i

                if self.solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def valid(self, bo, num, pos):
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return i, j

        return None
