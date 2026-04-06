class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[None for _ in range(cols)]for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if i == rows or j == cols:
                return 0
            if dp[i][j] != None:
                return dp[i][j]
            temp = 1
            for xi, xj in directions:
                row = xi+i
                col = xj+j
                if 0 <= row < rows and 0 <= col < cols and matrix[i][j] < matrix[row][col]:
                    temp = max(temp, 1+dfs(row, col))
            dp[i][j] = temp
            return dp[i][j]
        max_path = 0
        for row in range(rows):
            for col in range(cols):
                dfs(row, col)
                max_path = max(max_path, dp[row][col])
        # print(dp)
        return max_path