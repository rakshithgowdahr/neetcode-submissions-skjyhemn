class Solution:
    def backtrack(self, n, hash_map):
        if n == 1 or n == 2:
            return n
        if n in hash_map:
            return hash_map[n]
        res = self.backtrack(n-1, hash_map) + self.backtrack(n-2, hash_map)
        hash_map[n] = res
        return res
    def climbStairs(self, n: int) -> int:
        return self.backtrack(n, defaultdict(int))