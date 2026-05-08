class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums) #{5:4, 1:3}
        max_c = [-float('inf'), nums[0]]
        for key in c.keys():
            if c[key] > max_c[0]:
                max_c = [c[key], key]
        return max_c[1]
