class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(0, 0) (0, 1) (0, 2)   (0, 3)
        #(1, 0) (1, 1) (1, 2)   (1, 3)
        #(2, 0) (2, 1) (2, 2)   (2, 3)
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i//3,j//3)]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(i//3,j//3)].add(board[i][j])
        return True