class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        if not nums1:
            n = len(nums2)
            if n%2 == 1:
                return nums2[n//2]
            return (nums2[n//2]+nums2[(n//2)-1])/2
        if not nums2:
            n = len(nums1)
            if n%2 == 1:
                return nums1[n//2]
            return (nums1[n//2]+nums1[(n//2)-1])/2
        i, j = 0, 0
        num_len = len(nums1)+len(nums2) # 9%2 == 0 then 2 numbers else 1 number
        print(num_len)
        mid_point = (num_len//2) - (0 if num_len%2 == 1 else 1) # 9//2 = 4 10//2 = 5
        curr_count = 0
        print(mid_point)
        while i < len(nums1) or j < len(nums2):
            if curr_count >= mid_point:
                break
            curr_count += 1
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
        print(i, j, curr_count)
        if num_len%2 == 1:
            return min(nums1[i] if nums1 else nums2[j], nums2[j] if nums2 else nums1[i])
        else:
            n1 = nums1[i] if nums1 else nums2[i]
            n2 = nums2[j] if nums2 else nums1[j]
            return (n1+n2)/2