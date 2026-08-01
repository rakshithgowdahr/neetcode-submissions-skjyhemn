class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 != 0:
            return False
        def DFS(i, curr_sum):
            if curr_sum == total_sum/2:
                return True
            if i == len(nums):
                return False
            return DFS(i+1, curr_sum+nums[i]) or DFS(i+1, curr_sum)
        return DFS(0, 0)