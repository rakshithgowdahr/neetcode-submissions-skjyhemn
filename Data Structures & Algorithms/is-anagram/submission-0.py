class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapper = dict()
        for c in s:
            if c in mapper:
                mapper[c] += 1
            else:
                mapper[c] = 1
        for c in t:
            if c in mapper and mapper[c] > 0:
                mapper[c] -= 1
                continue
            return False
        return True