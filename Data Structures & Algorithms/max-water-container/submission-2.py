class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_cap = 0
        l, r = 0, len(heights)-1
        while l < r:
            water_cap = max(water_cap, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return water_cap