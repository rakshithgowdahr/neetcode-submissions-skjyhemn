class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bucket = [0] * 26
        t_bucket = [0] * 26
        for c in s:
            s_bucket[ord('a')-ord(c)] += 1
        for c in t:
            t_bucket[ord('a')-ord(c)] += 1
        return tuple(s_bucket) == tuple(t_bucket)