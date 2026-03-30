class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1
        s2_map = defaultdict(int)
        for i in range(len(s2)):
            s2_map[s2[i]] += 1
            if sum(list(s2_map.values())) > len(s1):
                s2_map[s2[i-len(s1)]] -= 1
            if sum(list(s2_map.values())) == sum(list(s1_map.values())):
                found = True
                for c in s1:
                    if c not in s2_map or s1_map[c] != s2_map[c]:
                        found = False
                        break
                if found:
                    return True
        return False