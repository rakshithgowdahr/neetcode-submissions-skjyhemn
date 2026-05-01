class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #behaviour of rotated sorted array
        #[5, 6, 0, 0, 1] -> l >= r and mid
        #[5, 6, 7, 0, 1] -> l >= r and mid >= l
        #[4, 0, 1, 2, 4] -> l >= r and 
        #if r < mid and r < l then rotation is on the right
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            # print(l, mid, r)
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                if target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            #rotation is in the right section
            elif nums[l] >= nums[r] and nums[mid] >= nums[l] and target < nums[l]:
                # print('l', target, nums[l])
                l = mid+1
            else:
                # print('r')
                r = mid-1
        return False