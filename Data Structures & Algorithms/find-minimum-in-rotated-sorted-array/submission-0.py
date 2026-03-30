class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            l_diff = abs(nums[l]-nums[mid])
            r_diff = abs(nums[r]-nums[mid])
            if (mid+1 >= len(nums) and nums[mid] <= nums[mid-1]) or (mid-1 < 0 and nums[mid] < nums[mid+1]) or (nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]):
                return nums[mid]
            if nums[l] > nums[r] and r_diff > l_diff:
                l = mid+1
            else:
                r = mid-1