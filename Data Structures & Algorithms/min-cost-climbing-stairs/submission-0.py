class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first_min = 0
        second_min = 0
        for i in range(len(cost)-1, -1, -1):
            temp = cost[i]+min(first_min, second_min)
            first_min, second_min  = temp, first_min
        return min(first_min, second_min)