class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(curr_arr, hash_set):
            if len(curr_arr) == n:
                res.append(curr_arr.copy())
                return
            for i in range(0, n):
                if i not in hash_set:
                    hash_set.add(i)
                    curr_arr.append(nums[i])
                    backtrack(curr_arr, hash_set)
                    hash_set.remove(i)
                    curr_arr.pop()
        backtrack([], set())
        return res