class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid[0])
        m = len(grid)
        def BFS(i, j, distance):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return
            if distance > grid[i][j]:
                return
            grid[i][j] = min(distance, grid[i][j])
            BFS(i+1, j, distance+1)
            BFS(i-1, j, distance+1)
            BFS(i, j+1, distance+1)
            BFS(i, j-1, distance+1)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    BFS(i, j, 0)