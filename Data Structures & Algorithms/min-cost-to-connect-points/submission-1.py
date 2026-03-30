class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {(x, y):[] for x, y in points }
        for xi, yi in points:
            for xj, yj in points:
                if (xi, yi) == (xj, yj):
                    continue
                cost = abs(xi - xj) + abs(yi - yj)
                adj[(xi, yi)].append([cost, (xj, yj)])
        min_heap = [(0, (points[0][0], points[0][1]) )]
        explored = set()
        max_cost = 0
        while min_heap:
            cost, point = heapq.heappop(min_heap)
            if point in explored:
                continue
            max_cost += cost
            explored.add(point)
            for nei_cost, nei_point in adj[point]:
                if nei_point not in explored:
                    heapq.heappush(min_heap, (nei_cost, nei_point))
        return max_cost