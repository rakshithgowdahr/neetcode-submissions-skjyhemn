class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        output = []
        for r in range(len(nums)):
            if r-l+1 == k:
                output.append(max(nums[l:r+1]))
                l += 1
        return output