class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        mid = (l+r) // 2
        while l <= r:
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
            mid = (l+r) // 2
        if abs(r-l) == 1:
            l -= 1
        for i in range(l, r+1):
            l1, r1 = 0, len(matrix[i])-1
            m = (l1+r1) // 2
            while l1 <= r1:
                if target == matrix[i][m]:
                    return True
                if target < matrix[i][m]:
                    r1 = m-1
                else:
                    l1 = m+1
                m = (l1+r1) // 2
        return False