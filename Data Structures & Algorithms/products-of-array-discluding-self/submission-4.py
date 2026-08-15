class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]
        prefix = 1
        postfix = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i+1]
        output = []
        for i in range(len(nums)):
            output.append(prefix*postfix[i])
            prefix *= nums[i]
        return output