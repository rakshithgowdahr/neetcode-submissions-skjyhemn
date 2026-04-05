class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, r_amt):
            if (i, r_amt) in cache:
                return cache[(i, r_amt)]
            if i == len(nums):
                return r_amt == 0
            cache[(i, r_amt)] = dfs(i+1, r_amt+nums[i]) + dfs(i+1, r_amt-nums[i])  
            return cache[(i, r_amt)]          
        return dfs(0, target)