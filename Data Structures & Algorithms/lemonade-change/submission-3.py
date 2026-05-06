class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5:0, 10:0}
        for bill in bills:
            print(counter)
            if bill == 5:
                counter[5] += 1
                continue
            if bill == 10:
                if counter[5] <= 0:
                    return False
                counter[5] -= 1
                counter[10] += 1
            else:
                if (counter[10] > 0 and counter[5] > 0) or counter[5] >= 3:
                    if counter[10] > 0:
                        counter[10] -= 1
                        counter[5] -= 1
                    else:
                        counter[5] -= 3
                else:
                    return False
        return True
                    