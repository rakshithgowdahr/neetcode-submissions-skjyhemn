class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        max_seq = 0
        for num in nums:
            max_seq = 1
            hash_set.add(num)
        for num in nums:
            if num-1 not in hash_set:
                seq = 1
                while num+1 in hash_set:
                    seq += 1
                    num += 1
                max_seq = max(max_seq, seq)
        return max_seq