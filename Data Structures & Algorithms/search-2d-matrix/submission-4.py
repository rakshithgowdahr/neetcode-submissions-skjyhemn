class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        mid = (l+r)//2
        while l <= r:
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                l = mid+1
            else:
                r = mid-1
            mid = (l+r)//2
        print(l, r)
        if abs(r-l) == 1:
            l -= 1
        l1, r1 = 0, len(matrix[l])-1
        while l1 <= r1:
            mid = (l1+r1)//2
            if matrix[l][mid] == target:
                return True
            if matrix[l][mid] < target:
                l1 = mid+1
            else:
                r1 = mid-1
        return False