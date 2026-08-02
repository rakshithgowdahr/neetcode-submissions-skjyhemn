class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        memo = dict()
        def dfs(i, j):
            nonlocal res
            if (i, j) in memo:
                return memo[(i, j)]
            output = 0
            if i == len(text1) or j == len(text2):
                memo[(i, j)] = 0
                return 0
            if text1[i] == text2[j]:
                output = 1+dfs(i+1, j+1)
            else:
                output = max(dfs(i+1, j), dfs(i, j+1))
            memo[(i, j)] = output
            return output
        return dfs(0, 0)