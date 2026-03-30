class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        max_time = 0
        while q:
            row, col, time = q.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row+1 < rows and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                q.append([row+1, col, time+1])
            if row-1 >= 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                q.append([row-1, col, time+1])
            if col+1 < cols and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                q.append([row, col+1, time+1])
            if col-1 >= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                q.append([row, col-1, time+1])
            max_time = max(max_time, time)
        # print(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return max_time
