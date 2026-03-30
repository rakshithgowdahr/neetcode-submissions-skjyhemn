class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1]* len(nums)
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix.append(nums[i]*(1 if i == 0 else prefix[i-1]))
        print(prefix)
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = (nums[i]*(1 if i == len(nums)-1 else postfix[i+1]))
        print(postfix)
        for i in range(len(nums)):
            output[i] = (1 if i== 0 else prefix[i-1]) * (1 if i== len(nums)-1 else postfix[i+1])
        return output