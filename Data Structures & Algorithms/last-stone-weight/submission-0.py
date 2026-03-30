class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            small1 = heapq.heappop(stones)
            small2 = heapq.heappop(stones)
            if abs(small1 - small2) != 0:
                heapq.heappush(stones, -(abs(small1-small2)))
        return -stones[0] if len(stones) else 0