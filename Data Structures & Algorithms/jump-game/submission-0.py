class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #[1, 2, 4, 2, 0, 0, 1]
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])#1 -> 2 -> 4
            if max_reach >= len(nums)-1:
                return True
        return True