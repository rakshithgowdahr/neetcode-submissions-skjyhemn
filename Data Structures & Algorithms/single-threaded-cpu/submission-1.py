class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        for i, task in enumerate(tasks):
            heapq.heappush(pending, [task, i]) #[[2, 1], 3]
        cpu_timer = 0
        output = []
        while pending or available:
            if pending and pending[0][0][0] > cpu_timer:
                cpu_timer = pending[0][0][0]
                continue
            while pending and pending[0][0][0] <= cpu_timer:
                task, index = heapq.heappop(pending)
                heapq.heappush(available, (task[1], index))
            if not available:
                continue
            processTime, index = heapq.heappop(available)
            cpu_timer += processTime
            output.append(index)
        return output
            