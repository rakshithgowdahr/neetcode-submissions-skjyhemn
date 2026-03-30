class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        while q:
            for i in range(len(q)):
                row, col, dist = q.popleft()
                if row+1 < rows and grid[row+1][col] == 2147483647:
                    grid[row+1][col] = dist+1
                    q.append((row+1, col, dist+1))
                if row-1 >= 0 and grid[row-1][col] == 2147483647:
                    grid[row-1][col] = dist+1
                    q.append((row-1, col, dist+1))
                if col+1 < cols and grid[row][col+1] == 2147483647:
                    grid[row][col+1] = dist+1
                    q.append((row, col+1, dist+1))
                if col-1 >= 0 and grid[row][col-1] == 2147483647:
                    grid[row][col-1] = dist+1
                    q.append((row, col-1, dist+1))
