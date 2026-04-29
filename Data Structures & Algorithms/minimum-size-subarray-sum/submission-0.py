class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #target = 7, nums = [2,3,1,2,4,3]
        #2, 3, 1, 2
        #3, 1, 2
        #3, 1, 2, 4
        #1, 2, 4
        #2, 4
        #2, 4, 3
        #4, 3
        i, j = 0, 0
        output = float('inf')
        curr_sum = 0
        while i < len(nums):
            print(curr_sum)
            print(i, j)
            if j < len(nums) and curr_sum < target:
                curr_sum += nums[j]
                j += 1
            else:
                curr_sum -= nums[i]
                i += 1
            if curr_sum >= target:
                output = min(output, j-i)
        return output if output != float('inf') else 0
