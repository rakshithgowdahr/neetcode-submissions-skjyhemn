class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        for i in range(len(height)-1):
            maxL.append(max(maxL[-1], height[i]))
        maxR = [0]
        for i in range(len(height)-1, 0, -1):
            maxR.insert(0, max(maxR[0], height[i]))
        max_water = 0
        for i, h in enumerate(height):
            limit = min(maxL[i], maxR[i])
            max_water += (limit-h if h <= limit else 0)
        return max_water