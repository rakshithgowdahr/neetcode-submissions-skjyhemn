class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_map = defaultdict(list)
        converted_points = []
        for point in points:
            value = math.sqrt((point[0]**2)+(point[1]**2))
            converted_points.append(value)
            hash_map[value].append(point)
        heapq.heapify(converted_points)
        output = []
        for i in range(k):
            value = heapq.heappop(converted_points)
            for val in hash_map[value]:
                output.append(val)
            del hash_map[value]
        return output