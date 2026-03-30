class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        def dfs(i, j, area):
            if (i, j) in visited or i < 0 or j < 0 or i == r or j == c or grid[i][j] == 0:
                return area
            visited.add((i, j))
            area1 = dfs(i+1, j, area)
            area2 = dfs(i-1, j, area)
            area3 = dfs(i, j+1, area)
            area4 = dfs(i, j-1, area)
            return 1+area1+area2+area3+area4
        for i in range(r):
            for j in range(c):
                area = dfs(i, j, 0)
                max_area = max(area, max_area)
        return max_area