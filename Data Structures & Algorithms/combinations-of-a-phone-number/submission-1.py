class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        key_pad = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        key_press = []
        for digit in digits:
            key_press.append(key_pad[digit])
        def backtrack(i, part_arr):
            if len(part_arr) == len(digits):
                res.append("".join(part_arr.copy()))
                return
            for j in range(i, len(key_press)):
                for k in range(0, len(key_press[j])):
                    part_arr.append(key_press[j][k])
                    backtrack(i+1, part_arr)
                    part_arr.pop()
                return
        backtrack(0, [])
        return res

