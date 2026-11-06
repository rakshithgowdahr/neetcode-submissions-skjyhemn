class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_c, white_c, blue_c = 0, 0, 0
        for num in nums:
            if num == 0:
                red_c += 1
            elif num == 1:
                white_c += 1
            else:
                blue_c += 1
        for i in range(len(nums)):
            num = None
            if red_c:
                num = 0
                red_c -= 1
            elif white_c:
                num = 1
                white_c -=1
            else:
                num = 2
                blue_c -= 1
            nums[i] = num