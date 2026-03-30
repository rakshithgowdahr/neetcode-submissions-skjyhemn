class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_key = [0] * 26
        for c in s1:
            key = ord(c)-ord("a")
            s1_key[key] = s1_key[key]+1
        s2_key = [0] * 26
        i = j = 0
        while j < len(s2):
            if j-i == len(s1):
                if tuple(s1_key) == tuple(s2_key):
                    return True
                s2_key[ord(s2[i])-ord("a")] = s2_key[ord(s2[i])-ord("a")]-1
                i += 1
                s2_key[ord(s2[j])-ord("a")] = s2_key[ord(s2[j])-ord("a")]+1
                j += 1
            else:
                s2_key[ord(s2[j])-ord("a")] = s2_key[ord(s2[j])-ord("a")]+1
                j += 1
        return tuple(s1_key) == tuple(s2_key)
