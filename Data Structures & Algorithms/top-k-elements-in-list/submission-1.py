class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        bucket = [[] for _ in range(len(nums)+1)]
        for key in hash_map:
            bucket[hash_map[key]].append(key)
        output = []
        for b in bucket[::-1]:
            for num in b:
                output.append(num)
                if len(output) >= k:
                    return output