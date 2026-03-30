class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(curr_arr, curr_sum, i):
            if curr_sum == target:
                res.append(curr_arr.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return
            curr_arr.append(candidates[i])
            backtrack(curr_arr, curr_sum+candidates[i], i+1)
            curr_arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(curr_arr, curr_sum, i+1)
        backtrack([], 0, 0)
        return res