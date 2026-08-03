class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        prev_sum = 0
        for i in range(len(nums)):
            if prev_sum+nums[i] > nums[i]:
                prev_sum = prev_sum+nums[i]
            else:
                prev_sum = nums[i]
            max_sum = max(max_sum, prev_sum)
        return max_sum
