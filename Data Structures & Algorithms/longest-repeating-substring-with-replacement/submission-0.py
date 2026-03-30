class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        output = 0
        l = 0
        for r in range(len(s)):
            hash_map[s[r]] += 1
            while (r-l+1) - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1
                l += 1
            output = max(output, r-l+1)
        return output