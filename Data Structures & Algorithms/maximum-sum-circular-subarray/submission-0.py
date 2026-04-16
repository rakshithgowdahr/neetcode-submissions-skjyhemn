class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0
        for num in nums:
            total += num
            curr_max = max(curr_max+num, num)
            curr_min = min(curr_min+num, num)
            globalMax = max(globalMax, curr_max)
            globalMin = min(globalMin, curr_min)
        return max(globalMax, total-globalMin) if globalMax > 0 else globalMax