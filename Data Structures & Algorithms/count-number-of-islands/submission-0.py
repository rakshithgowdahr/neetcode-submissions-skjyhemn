class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def DFS(i, j):
            if (i, j) in visited or grid[i][j] == "0":
                return 0
            visited.add((i, j))
            if i-1 >= 0:
                DFS(i-1, j)
            if i+1 < len(grid):
                DFS(i+1, j)
            if j-1 >= 0:
                DFS(i, j-1)
            if j+1 < len(grid[0]):
                DFS(i, j+1)
            return 1
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                output += DFS(i, j)
        return output