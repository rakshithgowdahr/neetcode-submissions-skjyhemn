class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #dict as trie
        #s as trie
        #1 trie or 2 trie
        cache = dict()
        words = set(dictionary)
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 0
            res = 1+dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1))
            cache[i] = res
            return res
        return dfs(0)