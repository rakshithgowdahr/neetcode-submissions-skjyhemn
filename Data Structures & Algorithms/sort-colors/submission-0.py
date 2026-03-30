class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b, c = 0, 0, 0
        for num in nums:
            if num == 0:
                a += 1
            if num == 1:
                b += 1
            if num == 2:
                c += 1
        for i, n in enumerate(nums):
            if a > 0:
                nums[i] = 0
                a -= 1
            elif b > 0:
                nums[i] = 1
                b -= 1
            elif c > 0:
                nums[i] = 2
                c -= 1