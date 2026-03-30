class Solution:
    def rob(self, nums: List[int]) -> int:
        #[1, 5, 1, 1, 10]
        cache = [None] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != None:
                return cache[i]
            cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return cache[i]
        return dfs(0)