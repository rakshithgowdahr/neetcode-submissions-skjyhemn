class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = {word for word in wordDict}
        cache = {}
        n = len(s)
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            for j in range(i, len(s)):
                if s[i:j+1] in dict_set:
                    if dfs(j+1):
                        cache[j] = True
                        return True
            cache[i] = False
            return False
        return dfs(0)