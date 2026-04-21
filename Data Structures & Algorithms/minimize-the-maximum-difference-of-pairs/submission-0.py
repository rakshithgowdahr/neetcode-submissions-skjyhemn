class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isAvailable(t):
            i = 0
            pairs = 0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= t:
                    pairs += 1
                    i += 2
                else:
                    i += 1
                if pairs == p:
                    return True
            return False
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = 0
        while l <= r:
            mid = (l+r) // 2
            if isAvailable(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
