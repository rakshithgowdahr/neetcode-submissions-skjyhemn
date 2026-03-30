class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float("-inf")
        l, r = 0, len(heights)-1
        while l < r:
            distance = r - l
            height = min(heights[l], heights[r])
            result = max(result, distance*height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result