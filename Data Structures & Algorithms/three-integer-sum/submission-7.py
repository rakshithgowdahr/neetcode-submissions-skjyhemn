class Solution:
    def twoSum(self, nums, target_i):
        hash_map = dict()
        output = []
        for i in range(len(nums)):
            if i == target_i:
                continue
            if nums[i] in hash_map:
                output.append([nums[i], hash_map[nums[i]]])
            hash_map[(-nums[target_i])-nums[i]] = nums[i]
        return output
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = dict()
        for i in range(len(nums)):
            output = self.twoSum(nums, i)
            for sums in output:
                hash_map[tuple(sorted([nums[i], sums[0], sums[1]]))] = [nums[i], sums[0], sums[1]]
        return [values for values in hash_map.values()]
