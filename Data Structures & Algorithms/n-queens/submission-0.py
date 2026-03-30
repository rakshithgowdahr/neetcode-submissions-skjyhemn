class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # top-left
    (-1, 1),  # top-right
    (1, -1),  # bottom-left
    (1, 1)    # bottom-right
        ]
        res = []
        board = [[0 for y in range(n)] for x in range(n)]
        def backtrack(i, curr_n):
            if i == n:
                output = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if board[i][j] == "Q":
                            s += "Q"
                        else: 
                            s += "."
                    output.append(s)
                res.append(output)
                return
            #place queen
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = "Q"
                    #update board
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        while 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] != "Q":
                                board[nx][ny] += 1
                            nx += dx
                            ny += dy
                    #place next queen in the current board
                    backtrack(i+1, curr_n-1)
                    #undo queen place action
                    board[i][j] = 0
                    #update board
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        while 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] != "Q":
                                board[nx][ny] -= 1
                            nx += dx
                            ny += dy
        backtrack(0, n)
        return res
        