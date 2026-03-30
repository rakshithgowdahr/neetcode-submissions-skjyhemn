class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = True
        return False