class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(word2):
                return len(word1)-i
            if i == len(word1):
                return len(word2)-j
            res = None
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                res = 1+min(
                dfs(i, j+1), # insert
                dfs(i+1, j+1), # replace
                dfs(i+1, j)) # remove
            cache[(i, j)] = res
            return res
        return dfs(0, 0)