class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        output = set()
        def simulate():
            pacific_reached, atlantic_reached = False, False
            while len(q):
                for _ in range(len(q)):
                    r, c = q.popleft()
                    visited.add((r, c))
                    if r == 0 or c == 0:
                        pacific_reached = True
                    if r == len(heights)-1 or c == len(heights[0])-1:
                        atlantic_reached = True
                    if pacific_reached and atlantic_reached:
                        return True
                    if (r-1, c) not in visited and r-1 >= 0 and heights[r-1][c] <= heights[r][c]:
                        if (r-1, c) in output:
                            return True
                        q.append((r-1, c))
                    if (r+1, c) not in visited and r+1 < len(heights) and heights[r+1][c] <= heights[r][c]:
                        if (r+1, c) in output:
                            return True
                        q.append((r+1, c))
                    if (r, c-1) not in visited and c-1 >= 0 and heights[r][c-1] <= heights[r][c]:
                        if (r, c-1) in output:
                            return True
                        q.append((r, c-1))
                    if (r, c+1) not in visited and c+1 < len(heights[0]) and heights[r][c+1] <= heights[r][c]:
                        if (r, c+1) in output:
                            return True
                        q.append((r, c+1))
            return pacific_reached and atlantic_reached
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                q.append((i, j))
                if(simulate()):
                    output.add((i, j))
                q.clear()
                visited = set()
        return [[r, c] for r, c in output]
        