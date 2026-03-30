class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket = [0] * 26
        for cs, ct in zip(s, t):
            bucket[ord(cs)-ord('a')] += 1
            bucket[ord(ct)-ord('a')] -= 1
        return all(v == 0 for v in bucket)