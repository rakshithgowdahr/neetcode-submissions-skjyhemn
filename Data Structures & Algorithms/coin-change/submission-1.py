class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        min_coins = float("inf")
        def dfs(i, amount, curr_coins):
            nonlocal min_coins
            if amount == 0:
                min_coins = min(min_coins, curr_coins)
                return
            if i == len(coins) or amount < 0 or curr_coins > min_coins:
                return
            dfs(i, amount-coins[i], curr_coins+1)
            for j in range(i+1, len(coins)):
                dfs(j, amount-coins[j], curr_coins+1)
        dfs(0, amount, 0)
        return min_coins if min_coins != float("inf") else -1