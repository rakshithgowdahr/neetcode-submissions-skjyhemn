class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def DFS(i, j, c):
            if c == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in visited:
                return False
            if word[c] != board[i][j]:
                return False
            visited.add((i, j))
            for direction in directions:
                x, y = direction
                if DFS(i+x, j+y, c+1):
                    return True
            visited.remove((i, j))
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if DFS(i, j, 0):
                        return True
        return False