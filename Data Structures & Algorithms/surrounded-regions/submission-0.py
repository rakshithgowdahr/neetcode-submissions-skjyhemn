class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def DFS(r, c):
            if (r, c) in visited or r < 0 or c <0 or r == ROWS or c == COLS or board[r][c] == "X":
                return
            visited.add((r, c))
            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)
        for c in range(COLS):
            if board[0][c] == "O":
                DFS(0, c)
            if board[ROWS-1][c] == "O":
                DFS(ROWS-1, c)
        for r in range(ROWS):
            if board[r][0] == "O":
                DFS(r, 0)
            if board[r][COLS-1] == "O":
                DFS(r, COLS-1)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = "X"