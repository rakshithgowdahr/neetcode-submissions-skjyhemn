class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 0,0 0,1 0,2 0,3
        # 1,0 1,1 1,2 1,3
        # 2,0 2,1 2,2 2,3
        # atlantic = last_col or last_row
        # pacific = col = 0 or row = 0

        rows, cols = len(heights), len(heights[0])
        def isPacific(i, j):
            return i == 0 or j == 0
        def isAtlantic(i, j):
            return i == rows-1 or j == cols-1
        output = []
        def dfs(i, j, isP, isA, visited):
            if (i,j) in visited or i < 0 or j < 0 or i == rows or j == cols:
                return (isP, isA)
            visited.add((i, j))
            is_Pacific = isP if isP else isPacific(i, j)
            is_Atlantic = isA if isA else isAtlantic(i, j)
            if is_Pacific and is_Atlantic:
                return (True, True)
            p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = False
            if i+1 < rows and heights[i+1][j] <= heights[i][j]:
                p1, p2 = dfs(i+1, j, is_Pacific, is_Atlantic, visited)
            if i-1 >= 0 and heights[i-1][j] <= heights[i][j]:
                p3, p4 = dfs(i-1, j, is_Pacific, is_Atlantic, visited)
            if j+1 < cols and heights[i][j+1] <= heights[i][j]:
                p5, p6 = dfs(i, j+1, is_Pacific, is_Atlantic, visited)
            if j-1 >= 0 and heights[i][j-1] <= heights[i][j]:
                p7, p8 = dfs(i, j-1, is_Pacific, is_Atlantic, visited)
            return (is_Pacific or p1 or p3 or p5 or p7, is_Atlantic or p2 or p4 or p6 or p8)
            
        for i in range(rows):
            for j in range(cols):
                isP, isA = dfs(i, j, False, False, set())
                if isP and isA:
                    output.append([i, j])
        return output
            