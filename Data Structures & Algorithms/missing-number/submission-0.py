class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _sum = 0
        n = len(nums)
        for num in nums:
            _sum += num
        return int((n*((n+1)/2))-_sum)