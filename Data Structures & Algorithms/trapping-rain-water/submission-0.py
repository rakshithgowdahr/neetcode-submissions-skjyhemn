class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        maxR = [0]
        minLR = []
        for i in range(1, len(height)):
            maxL.append(max(height[i-1], maxL[-1]))
            maxR = [max(height[len(height)-i], maxR[0])] + maxR
        for i in range(len(height)):
            minLR.append(min(maxL[i], maxR[i]))
        water = 0
        for i in range(len(minLR)):
            water += (minLR[i]-height[i]) if (minLR[i]-height[i]) > 0 else 0
        return water