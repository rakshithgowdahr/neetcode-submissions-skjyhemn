class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(curr_coin, i):
            if i >= len(prices):
                return 0
            if (curr_coin, i) in cache:
                return cache[(curr_coin, i)]
            if curr_coin == None:
                cache[(curr_coin, i)] = max(dfs(prices[i], i+1), dfs(curr_coin, i+1))
            else:
                #sell now/don't sell now
                curr_profit = prices[i] - curr_coin if curr_coin < prices[i] else 0
                cache[(curr_coin, i)] =  max((curr_profit + dfs(None, i+2)) if curr_profit else dfs(curr_coin, i+1), dfs(curr_coin, i+1))
            return cache[(curr_coin, i)]
        return dfs(None, 0)