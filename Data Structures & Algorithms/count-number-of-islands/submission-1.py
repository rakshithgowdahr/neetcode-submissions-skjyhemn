class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        output = 0
        def DFS(i, j):
            if (i,j) in visited or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            visited.add((i,j))
            DFS(i+1, j)
            DFS(i-1, j)
            DFS(i, j+1)
            DFS(i, j-1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    DFS(i, j)
                    output += 1
        return output