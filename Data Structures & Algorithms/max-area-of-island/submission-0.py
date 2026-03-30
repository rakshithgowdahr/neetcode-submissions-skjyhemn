class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        output = 0
        def DFS(i, j):
            if (i, j) in visited or grid[i][j] == 0:
                return
            visited.add((i, j))
            if i-1 >= 0:
                DFS(i-1, j)
            if i+1 < len(grid):
                DFS(i+1, j)
            if j-1 >= 0:
                DFS(i, j-1)
            if j+1 < len(grid[0]):
                DFS(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prev = len(visited)
                DFS(i, j)
                after = len(visited)
                output = max(output, after-prev)
        return output