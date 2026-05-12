class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (C+1) for _ in range(R+1)]

        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c+1]
                self.sum_mat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.sum_mat[r2][c2]
        above_sqr = self.sum_mat[r1-1][c2]
        left_sqr = self.sum_mat[r2][c1-1]
        overlap = self.sum_mat[r1-1][c1-1]
        return bottom_right - above_sqr - left_sqr + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)