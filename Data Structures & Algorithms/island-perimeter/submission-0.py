class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    # if i-1 >= 0 and grid[i-1][j] != 0:
                    #     grid[i-1][j] -= 0.25
                    #     grid[i][j] -= 0.25
                    if i+1 < rows and grid[i+1][j] != 0:
                        grid[i+1][j] -= 0.25
                        grid[i][j] -= 0.25
                    # if j-1 >= 0 and grid[i][j-1] != 0:
                    #     grid[i][j-1] -= 0.25
                    #     grid[i][j] -= 0.25
                    if j+1 < cols and grid[i][j+1] != 0:
                        grid[i][j+1] -= 0.25
                        grid[i][j] -= 0.25
                    total += (grid[i][j]*4)
        return int(total)