class Solution:
    def twoSum(self, nums, target):
        hash_map = dict()
        output = set()
        for num in nums:
            if num in hash_map:
                output.add((num, hash_map[num]))
            else:
                hash_map[target-num] = num
        return [list(x) for x in output]
    def threeSum(self, nums, target):
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res = self.twoSum(nums[i+1:], target-nums[i])
            for a, b in res:
                output.append([a, b, nums[i]])
        return output
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #[-3, 0, 1, 2, 3, 3]
        #[-1, -1, -1, 1, 1, 1]
        output = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res = self.threeSum(nums[i+1:], target-nums[i])
            for a, b, c in res:
                output.append([a, b, c, nums[i]])
        return output
        