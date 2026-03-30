class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        i, j = 0, len(heights)-1
        while i < j:
            curr_water = min(heights[i], heights[j]) * (j-i)
            output = max(output, curr_water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return output