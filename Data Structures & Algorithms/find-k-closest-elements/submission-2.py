class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [2, 4, 5, 8], k = 3, x = 6
        # [2, 4, 5, 8], k = 2, x = 7
        #find the place of x in the arr
        #expand outwards, either left or right
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        for i in range(len(arr)):
            if arr[i] == x or arr[i] < x < arr[i+1]:
                l = r = i if arr[i] == x or x-arr[i] <= arr[i+1]-x else i+1
                while r-l-1 < k:
                    if l < 0:
                        r += 1
                    elif r >= len(arr):
                        l -= 1
                    elif abs(arr[l]-x) <= abs(arr[r]-x):
                        l -= 1
                    else:
                        r += 1
                return arr[l+1:r]
        