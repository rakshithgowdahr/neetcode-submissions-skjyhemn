class Solution:
    def numDecodings(self, s: str) -> int:
        # 456 -> [4, 5, 6] [45, 6] x [4, 56] x = 1
        #1002 -> x
        # 222 -> [2, 2, 2] [2, 22] [22, 2] = 3
        # 236 -> [2, 3, 6] [2, 36] x [23, 6] = 2        
        # 2122 -> [2, 1, 2, 2] [2, 1, 22] [2, 12, 2] [21, 2, 2] [21, 22]
        # 122 -> [1, 22] [12, 2]
        memo = dict()
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if i+1 < len(s):
                if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                    res += dfs(i+2)
            memo[i] = res
            return res
        return dfs(0)