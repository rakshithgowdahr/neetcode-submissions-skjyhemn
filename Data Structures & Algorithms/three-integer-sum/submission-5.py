class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        hash_map = set()
        l = 0
        while l <= len(nums)-2:
            l1, r1 = l+1, len(nums)-1
            while l1 < r1:
                cur_sum = sorted_nums[l]+sorted_nums[l1]+sorted_nums[r1]
                if cur_sum == 0:
                    temp = [sorted_nums[l], sorted_nums[l1], sorted_nums[r1]]
                    if tuple(temp) not in hash_map:
                        output.append(temp)
                        hash_map.add(tuple(temp))
                    l1 += 1
                    r1 -= 1
                if cur_sum < 0:
                    l1 += 1
                if cur_sum > 0:
                    r1 -= 1
            l += 1
        return output