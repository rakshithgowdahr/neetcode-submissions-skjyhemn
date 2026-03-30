class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = defaultdict(int)
        for task in tasks:
            hash_map[task] += 1
        max_heap = [-value for value in hash_map.values()]#[3, 2, 2, 1]
        heapq.heapify(max_heap)
        output, QUEUE = 0, []
        while len(max_heap) or len(QUEUE):
            output += 1
            if len(max_heap):
                count = 1 + heapq.heappop(max_heap)
                if count:
                    QUEUE.append([count, output+n])
            if len(QUEUE) and QUEUE[0][1] == output:
                heapq.heappush(max_heap, QUEUE.pop(0)[0])
        return output