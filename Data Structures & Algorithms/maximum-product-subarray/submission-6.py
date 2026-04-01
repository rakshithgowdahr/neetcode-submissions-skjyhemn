class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #[-2, 3, -4]
        curr_max, curr_min = 1, 1
        res = -float('inf')
        for num in nums:
            temp = curr_max*num
            curr_max = max(temp, num*curr_min, num)
            curr_min = min(temp, num*curr_min, num)
            res = max(res, curr_max)
        return res