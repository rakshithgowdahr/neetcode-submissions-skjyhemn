class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            # Safely check if left and right neighbors are smaller (or don't exist)
            left_smaller = (mid == 0 or nums[mid] > nums[mid - 1])
            right_smaller = (mid == len(nums) - 1 or nums[mid] > nums[mid + 1])
            
            if left_smaller and right_smaller:
                return mid
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1