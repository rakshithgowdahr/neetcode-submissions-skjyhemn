class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if (nums[mid] < nums[r] and target > nums[mid] and target < nums[r]) or (nums[mid] > nums[r] and (target > nums[mid] or target < nums[r])):
                l = mid+1
            else:
                r = mid-1
        return -1