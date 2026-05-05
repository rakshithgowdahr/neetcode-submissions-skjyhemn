class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #divide array into equal subset sum
        #[1, 1, 2, 2, 2] -> 8/4 = each side should be 2
        #[3, 3, 3, 3, 4] -> 16/4 = each side should be 4
        sticks_sum = sum(matchsticks)
        side_len = sticks_sum // 4
        if sticks_sum / 4 != side_len:
            return False
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        def backtrack(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= side_len:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)