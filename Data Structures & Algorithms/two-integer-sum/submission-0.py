class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = dict()
        for i in range(0, len(nums)):
            inv = target - nums[i]
            if inv in mapper:
                return [mapper[inv], i]
            mapper[nums[i]] = i
            print(mapper)
        return [0,0]