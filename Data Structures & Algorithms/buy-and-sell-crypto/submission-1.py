class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 1
        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            max_profit = max(max_profit, curr_profit)
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
        return max_profit