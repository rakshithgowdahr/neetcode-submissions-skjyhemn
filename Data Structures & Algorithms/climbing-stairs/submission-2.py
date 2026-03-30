class Solution:
    def climb(self, n, cache):
        if n < 3:
            return n
        if n in cache:
            return cache[n]
        res = self.climb(n-1, cache) + self.climb(n-2, cache)
        cache[n] = res
        return res
    def climbStairs(self, n: int) -> int:
        return self.climb(n, dict())