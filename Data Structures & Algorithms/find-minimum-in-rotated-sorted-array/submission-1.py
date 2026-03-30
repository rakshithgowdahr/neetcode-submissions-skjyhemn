class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, mid, r
        # if mid > r move to right section
        # if mid < r move to left section
        # if mid < l
        # if mid > l
        l, r = 0, len(nums)-1
        min_num = float('inf')
        while l <= r:
            mid = (l+r)//2
            min_num = min(min_num, nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid-1
        return min_num