class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #column validity 
        # [0, 0] [1, 0] [2, 0] [3, 0]
        # [0, 1] [1, 1] [2, 1] [3, 1]
        # [0, 2] [1, 2] [2, 2] [3, 1]
        for i in range(len(board)):
            hash_set = set()
            for j in range(len(board)):
                if board[j][i] in hash_set:
                    return False
                if board[j][i] != ".":
                    hash_set.add(board[j][i])
        #row validity
        for i in range(len(board)):
            hash_set = set()
            for j in range(len(board)):
                if board[i][j] in hash_set:
                    return False
                if board[i][j] != ".":
                    hash_set.add(board[i][j])
        #block validity
        mov = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        p = 0
        while p < len(board):
            i, j = mov[p]
            hash_set = set()
            for x in range(i, i+3):
                for y in range(j , j+3):
                    if board[x][y] in hash_set:
                        return False
                    if board[x][y] != ".":
                        hash_set.add(board[x][y])
            p += 1
        return True