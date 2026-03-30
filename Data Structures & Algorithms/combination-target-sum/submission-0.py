class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr_sum, i, curr_arr):
            if i == len(nums):
                return
            curr_sum += nums[i]
            curr_arr.append(nums[i])
            if curr_sum > target:
              curr_sum -= nums[i]
              curr_arr.pop()
              return
            if curr_sum == target:
              res.append(curr_arr.copy())
            backtrack(curr_sum, i, curr_arr)
            last_item = curr_arr.pop()
            curr_sum -= last_item
            backtrack(curr_sum, i+1, curr_arr)
        backtrack(0, 0, [])
        return res
