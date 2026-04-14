class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        [[2, 3, 2], [1, 2, 3], [3, 3, 5]]
        ax, bx, cx = target
        for j in range(1, len(triplets)):
            ai, bi, ci = triplets[j-1]
            aj, bj, cj = triplets[j]
            if ai > ax or bi > bx or ci > cx:
                continue
            if aj > ax or bj > bx or cj > cx:
                triplets[j][0] = ai
                triplets[j][1] = bi
                triplets[j][2] = ci
                continue
            triplets[j][0] = max(ai, aj)
            triplets[j][1] = max(bi, bj)
            triplets[j][2] = max(ci, cj)
        # print(triplets[-1])
        return triplets[-1] == target