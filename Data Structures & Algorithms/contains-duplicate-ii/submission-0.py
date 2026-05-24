class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i, num in enumerate(nums):
            if num in hash_map:
                index = hash_map[num]
                if abs(index-i) <= k:
                    return True
            hash_map[num] = i
        return False