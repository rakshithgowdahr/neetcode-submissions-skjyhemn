class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = defaultdict(int)
        i = j = 0
        max_len = 0
        while j < len(s):
            if s[j] not in hash_map:
                hash_map[s[j]] = j
                max_len = max(max_len, j-i+1)
                j += 1
            else:
                jump_to = hash_map[s[j]]+1
                for x in range(i, jump_to):
                    del hash_map[s[x]]
                i = jump_to
        return max_len
                