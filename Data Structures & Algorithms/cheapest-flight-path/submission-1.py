class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices[:]
            for frm, to, cost in flights:
                if prices[frm] == float("inf"):
                    continue
                if prices[frm] + cost < temp_prices[to]:
                    temp_prices[to] = prices[frm]+cost
            prices = temp_prices
        return prices[dst] if prices[dst] != float("inf") else -1