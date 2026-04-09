class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curr_total = 0
        start_at = 0
        for i in range(len(gas)):
            curr_total += (gas[i] - cost[i])
            if curr_total < 0:
                curr_total = 0
                start_at = i+1
        return start_at