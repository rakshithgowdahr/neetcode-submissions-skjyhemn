class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        store = [[] for _ in range(len(nums)+1)]
        for key in hash_map.keys():
            store[hash_map[key]].append(key)
        output = []
        for i in range(len(store)-1, -1, -1):
            for j in range(len(store[i])-1, -1, -1):
                    output.append(store[i][j])
                    if len(output) >= k:
                        return output
