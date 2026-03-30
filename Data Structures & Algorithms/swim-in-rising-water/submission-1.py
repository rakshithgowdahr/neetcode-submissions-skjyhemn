class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [[grid[0][0], (0, 0)]]
        explored = defaultdict(int)
        while min_heap:
            height, point = heapq.heappop(min_heap)
            if point in explored:
                continue
            x, y = point
            explored[point] = height
            for dx, dy in directions:
                r, c = dx+x, dy+y
                if r < 0 or r == rows or c < 0 or c == cols or (r, c) in explored:
                    continue
                heapq.heappush(min_heap, [max(height, grid[r][c]), (r,c)])
        return explored[(rows-1, cols-1)]