class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        #1. [1, 5, 5, 9] half sum from (1, 10)
        #2. [4, 2, 8, 2] half sum from (1, 8)
        #3. [1, 2, 3, 4] half sum from (1, 5)
        #sum/2
        half_sum = total_sum // 2
        dp = [False] * (half_sum+1)
        dp[0] = True
        for num in nums:
            for i in range(half_sum, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        return dp[half_sum]