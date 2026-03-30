class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for key in hash_map:
                if hash_map[key] <= 0:
                    continue
                subset.append(key)
                hash_map[key] -= 1
                dfs(subset)
                subset.pop()
                hash_map[key] += 1
        dfs([])
        return res