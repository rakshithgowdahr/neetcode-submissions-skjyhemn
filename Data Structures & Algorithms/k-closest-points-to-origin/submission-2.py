class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2+point[1]**2)
            heapq.heappush(heap, (dist, point[0], point[1]))
        output = []
        for _ in range(k):
            dist, x1, y1 = heapq.heappop(heap)
            output.append([x1, y1])
        return output