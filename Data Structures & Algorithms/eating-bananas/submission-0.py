class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_p = 1
        max_p = max(piles)
        mid = (min_p + max_p)//2
        output = float("inf")
        while min_p <= max_p:
            current_h = 0
            for p in piles:
                current_h += math.ceil(p / mid)
            if current_h <= h:
                output = mid
                max_p = mid-1
            if current_h > h:
                min_p = mid+1
            mid = (min_p + max_p)//2
        return output