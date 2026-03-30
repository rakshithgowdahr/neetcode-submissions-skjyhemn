class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for src, dst, time in times:
            adj[src].append((dst, time))
        min_heap = [[0, k]]
        shortest = {}
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in shortest:
                continue
            shortest[node] = time
            for nei, nei_time in adj[node]:
                if nei not in shortest:
                    heapq.heappush(min_heap, [nei_time+time, nei])
        max_time = -1
        for i in range(1, n+1):
            if i not in shortest:
                return -1
            max_time = max(max_time, shortest[i])
        return max_time
            