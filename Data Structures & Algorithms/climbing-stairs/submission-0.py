class Solution:
    def climb(self, n, hash_map):
        if n <= 1:
            return 1
        if n in hash_map:
            return hash_map[n]
        n1 = self.climb(n-1, hash_map)
        n2 = self.climb(n-2, hash_map)
        hash_map[n] = n1+n2
        return n1+n2
    def climbStairs(self, n: int) -> int:
        return self.climb(n, dict())