class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                return sorted_nums[i]