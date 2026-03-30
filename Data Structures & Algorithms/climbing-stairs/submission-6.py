class Solution:
    def climbStairs(self, n: int) -> int:
        #n = 1 -> 1
        #n = 2 -> 2
        #n = 3 -> 3
        def climb(n, memo):
            if n in memo:
                return memo[n]
            if n <= 2:
                return n
            ways =  climb(n-1, memo) +  climb(n-2, memo)
            memo[n] = ways
            return ways
        return climb(n, dict())