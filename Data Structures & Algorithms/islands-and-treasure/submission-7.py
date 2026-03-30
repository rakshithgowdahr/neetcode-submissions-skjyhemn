class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid[0])
        m = len(grid)
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        def addGrid(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1 or (i, j) in visited:
                return
            visited.add((i, j))
            q.append((i, j))
        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addGrid(i+1, j)
                addGrid(i-1, j)
                addGrid(i, j+1)
                addGrid(i, j-1)
            dist += 1