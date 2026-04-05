class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #min coins vs different ways
        cache = {}
        def dfs(amt, i):
            if (amt, i) in cache:
                return cache[(amt, i)]
            if amt == 0:
                return 1
            if amt < 0 or i == len(coins):
                return 0
            cache[(amt, i)] = dfs(amt-coins[i], i) + dfs(amt, i+1)
            return cache[(amt, i)]
        return dfs(amount, 0)