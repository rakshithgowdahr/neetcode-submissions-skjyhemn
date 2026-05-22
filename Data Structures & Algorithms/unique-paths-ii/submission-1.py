class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = dict()
        M, N = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > M or j > N or obstacleGrid[i][j] == 1:
                return 0
            if i == M and j == N :
                return 1
            p1 = dfs(i+1, j)
            p2 = dfs(i, j+1)
            memo[(i, j)] = p1+p2
            return p1+p2
        return dfs(0, 0)