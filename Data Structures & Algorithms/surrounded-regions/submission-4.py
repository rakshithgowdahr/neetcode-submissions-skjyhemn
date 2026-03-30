class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or (i,j) in visited or board[i][j] == "X": 
                return
            visited.add((i, j))
            for rx, cx in directions:
                dfs(i+rx, j+cx)
                    
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0 or row == rows-1 or col == cols-1) and board[row][col] == "O":
                    dfs(row, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"