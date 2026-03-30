class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums)*2)
        n = len(nums)
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+n] = num
        return ans