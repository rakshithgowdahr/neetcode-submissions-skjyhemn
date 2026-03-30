class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        max_length = 0
        hash_map = defaultdict(int)
        while j < len(s):
            if s[j] not in hash_map:
                max_length = max(max_length, j-i+1)
                hash_map[s[j]] = j
                j += 1
            else:
                i = hash_map[s[j]]+1
                j = i
                hash_map = defaultdict(int)
        return max_length