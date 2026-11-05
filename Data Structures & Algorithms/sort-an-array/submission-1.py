class Solution:
    def mergeTwoSorted(self, arr1, arr2):
        i, j = 0, 0
        output = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                output.append(arr1[i])
                i += 1
            else:
                output.append(arr2[j])
                j += 1
        if i < len(arr1):
            output = output + arr1[i:]
        if j < len(arr2):
            output = output + arr2[j:]
        return output
    def divide(self, nums):
        if len(nums) <= 1:
            return nums
        if len(nums) <= 2:
            return nums if nums[0] <= nums[1] else [nums[1], nums[0]]
        arr1 = self.divide(nums[:len(nums)//2])
        arr2 = self.divide(nums[len(nums)//2:])
        return self.mergeTwoSorted(arr1, arr2)
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide(nums)
        