class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        # 999 -> 1000 => 9 -> 10 carry 1 -> 9 +1 = 10
        # 9 -> 10
        # 89 -> 90
        # 99 -> 100
        # 1089 -> 1090
        output = []
        num = 1
        for i in range(len(digits)-1, -1, -1):
            if (digits[i]+num)% 10 == 0:
                num = 1
                output.append(0)
            else:
                output.append(digits[i]+num)
                num = 0
        if num:
            output.append(1)
        return output[::-1]
