class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = dict()
        for n in nums:
            if n in hash_map:
                return True
            else:
                hash_map[n] = True
        return False