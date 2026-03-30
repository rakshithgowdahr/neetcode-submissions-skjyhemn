class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = dict()
        for i, pos in enumerate(position):
            speed_map[pos] = speed[i]
        position.sort()
        pred_target = []
        for pos in position:
            pred_target.append(((target-pos)/speed_map[pos]))
        fleet = 1
        curr_max = pred_target[-1]
        for i in range(len(pred_target)-2, -1, -1):
            if pred_target[i] > curr_max:
                curr_max = pred_target[i]
                fleet += 1
        return fleet