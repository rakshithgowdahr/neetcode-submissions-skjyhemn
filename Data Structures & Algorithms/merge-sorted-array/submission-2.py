class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #[1,2,3,0,0,0] [2,5,6]
        #[10,20,20,40,0,0] [1,2]
        i, j, k = m-1, len(nums2)-1, len(nums1)-1
        while j >= 0:
            temp = nums1[i] if i >= 0 else -float('inf')
            if temp >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
