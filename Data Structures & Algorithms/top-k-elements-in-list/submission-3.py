class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        heap = []
        for key in counter.keys():
            heapq.heappush(heap, [-1*counter[key], key])
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
