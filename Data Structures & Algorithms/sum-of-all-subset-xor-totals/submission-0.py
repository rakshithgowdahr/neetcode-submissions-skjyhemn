class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        #xor_sum = 0
        #xor_sum = 0 ^ 2 = 2
        #xor_sum = 2
        def backtrack(i, xor_sum):
            nonlocal total
            if i == len(nums):
                total += xor_sum
                return
            xor = xor_sum ^ nums[i]
            backtrack(i+1, xor)
            backtrack(i+1, xor_sum)
        backtrack(0, 0)
        return total