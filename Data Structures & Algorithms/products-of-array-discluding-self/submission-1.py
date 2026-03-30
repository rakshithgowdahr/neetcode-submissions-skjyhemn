class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        postfix_sum = []
        output = []
        for i, num in enumerate(nums):
            prefix_sum.append(num*prefix_sum[-1] if len(prefix_sum) else nums[0])
            postfix_sum = [nums[len(nums)-i-1]*postfix_sum[0] if len(postfix_sum) else nums[-1]] + postfix_sum
        for i in range(len(nums)):
            output.append((prefix_sum[i-1] if i > 0 else 1)*(postfix_sum[i+1] if i+1 < len(nums) else 1))
        return output