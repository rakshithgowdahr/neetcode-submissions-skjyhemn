class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #include first house and exclude last
        rob1, rob2 = 0, 0
        for i in range(len(nums)-1):
            rob1, rob2 = rob2, max(nums[i]+rob1, rob2)
        final_rob = rob2
        #include last house and exclude first
        rob1, rob2 = 0, 0
        for i in range(1, len(nums)):
            rob1, rob2 = rob2, max(nums[i]+rob1, rob2)
        return max(final_rob, rob2)
