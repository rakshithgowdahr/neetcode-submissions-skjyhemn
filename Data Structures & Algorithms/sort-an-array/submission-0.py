class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            output = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    output.append(arr1[i])
                    i += 1
                else:
                    output.append(arr2[j])
                    j += 1
            if i < len(arr1):
                output += arr1[i:]
            if j < len(arr2):
                output += arr2[j:]
            return output
        def dfs(arr):
            if len(arr) <= 1:
                print(arr)
                return arr
            n = len(arr)
            res1 = dfs(arr[:n//2])
            res2 = dfs(arr[(n//2):])
            return merge(res1, res2)
        return dfs(nums)