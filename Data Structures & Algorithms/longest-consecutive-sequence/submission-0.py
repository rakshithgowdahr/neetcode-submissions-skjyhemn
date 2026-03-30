class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        i = 0
        store = set(nums)
        while i < len(nums):
            num = nums[i]
            start = 1
            while True:
                if num-1 in store:
                    start += 1
                    num -= 1
                else:
                    break
            seq = max(seq, start)
            i += 1
        return seq
