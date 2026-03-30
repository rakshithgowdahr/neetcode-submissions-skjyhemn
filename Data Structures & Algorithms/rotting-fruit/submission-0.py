class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        def addCell(r, c):
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or
                (r, c) in visited or grid[r][c] == 0
            ):
                return
            visited.add((r, c))
            q.append([r, c])
        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                addCell(i + 1, j)
                addCell(i - 1, j)
                addCell(i, j + 1)
                addCell(i, j - 1)
            dist += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return dist-1 if len(visited) else dist