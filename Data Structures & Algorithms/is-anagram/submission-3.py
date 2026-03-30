class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = dict()
        for _s in s:
            if _s in hm:
                hm[_s] += 1
            else:
                hm[_s] = 1
        for _t in t:
            if _t in hm and hm[_t] > 0:
                hm[_t] -= 1
            else:
                return False
        return True