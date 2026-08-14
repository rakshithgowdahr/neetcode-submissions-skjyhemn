class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sort by count
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        counter = []
        for key in hash_map:
            counter.append([hash_map[key], key])
        counter.sort(reverse=True)
        output = []
        for i in range(k):
            output.append(counter[i][1])
        return output