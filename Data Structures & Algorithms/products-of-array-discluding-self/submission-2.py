class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for i in range(len(nums)-2, -1, -1):
            postfix.insert(0, postfix[0]*nums[i])
        output = []
        for i in range(len(nums)):
            left = 1 if i-1 < 0 else prefix[i-1]
            right = 1 if i+1 > len(nums)-1 else postfix[i+1]
            output.append(left * right)
        return output

