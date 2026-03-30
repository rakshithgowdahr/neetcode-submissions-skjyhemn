class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #A B C E
        #S F C S
        #A D E E
        n = len(board)
        m = len(board[0])
        def dfs(i, j, wi, visited):
            if wi == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited:
                return False
            if board[i][j] != word[wi]:
                return False
            visited.add((i, j))
            found = (dfs(i+1, j, wi+1, visited) or
            dfs(i-1, j, wi+1, visited) or
            dfs(i, j+1, wi+1, visited) or
            dfs(i, j-1, wi+1, visited))
            visited.remove((i, j))
            return found
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0, set()):
                    return True
        return False