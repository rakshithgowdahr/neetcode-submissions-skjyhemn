class Solution:
    def totalNQueens(self, n: int) -> int:
        # Q -> queen placement
        # . -> place available
        board = [["." for _ in range(n)] for _ in range(n)]
        queen_placements = 0
        def isAvailable(row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            r, c = row, col
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            return True
        def dfs(row):
            nonlocal queen_placements
            if row == n:
                queen_placements += 1
                return
            for col in range(n):
                if isAvailable(row, col):
                    board[row][col] = "Q"
                    dfs(row+1)
                    board[row][col] = "."
            
        dfs(0)
        return queen_placements