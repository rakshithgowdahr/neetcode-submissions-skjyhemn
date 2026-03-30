class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            hash_set.add(num)
        i = 0
        max_seq = 0
        for num in nums:
            seq = 1
            curr_num = num
            while curr_num-1 in hash_set:
                seq += 1
                curr_num -= 1
            max_seq = max(seq, max_seq)
        return max_seq
