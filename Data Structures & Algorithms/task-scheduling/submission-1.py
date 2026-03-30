class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        max_heap = [val*-1 for val in counter.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time+n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time