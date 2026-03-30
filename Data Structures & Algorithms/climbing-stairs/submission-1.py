class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        a1, a2 = 1, 2
        for i in range(2, n):
            temp = a1 + a2
            a1, a2 = a2, temp
        return a2