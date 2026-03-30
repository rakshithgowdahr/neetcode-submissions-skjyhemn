class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #1,25
        min_speed = float("inf")
        while l <= r:
            speed = (l+r)//2 #13
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/speed)
                if time_taken > h:
                    break
            # time_taken = 6
            # 6 <= 4 no,min_k = min(25, 6)
            # print("time_taken =", time_taken)
            # print("speed = ", speed)
            if time_taken > h:
                l = speed+1
            else:
                min_speed = min(min_speed, speed)
                r = speed-1
        return min_speed            