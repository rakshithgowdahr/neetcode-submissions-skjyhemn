class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, stone*-1)
        while len(heap) > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, abs(y-x)*-1)
        return heap[0]*-1 if heap else 0