class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l, r = 0, nums[0]
        jumps = 1
        while r < len(nums)-1:
            max_jump = 0
            #within the range l to r, pick the farthest I can jump and update l
            for i in range(l+1, len(nums) if r+1 > len(nums) else r+1):
                if i+nums[i] > max_jump:
                    max_jump = i+nums[i]
                    l = i
            r = max_jump
            jumps += 1
        return jumps