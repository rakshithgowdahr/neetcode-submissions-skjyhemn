class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            curr_max_area = heights[i]
            for j in range(i, len(heights)):
                curr_max_area = min(curr_max_area, heights[j])
                max_area = max(max_area, curr_max_area*(j-i+1))
        return max_area