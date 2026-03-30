class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # IN = [1,2,3,2,2]
        # [-1, -2, -3, 2, 2]
        for num in nums:
            index = abs(num)-1 #0 indexing
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1