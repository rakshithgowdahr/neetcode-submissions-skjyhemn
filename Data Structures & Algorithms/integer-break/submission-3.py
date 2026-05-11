class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        memo = dict()
        def dfs(num):
            if num <= 3:
                return num
            if num in memo:
                return memo[num]
            res = 0
            for i in range(2, (num // 2) + 1):
                res = max(res, i * (num - i), i * dfs(num - i))
            memo[num] = res
            return res
        return dfs(n)