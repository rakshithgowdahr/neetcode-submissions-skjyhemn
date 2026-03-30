class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(comb_arr, op, cl):
            if op == n and cl == n:
                res.append("".join(comb_arr.copy()))
                return
            if op < n:
                comb_arr.append("(")
                backtrack(comb_arr, op+1, cl)
                comb_arr.pop()
            if cl < op:
                comb_arr.append(")")
                backtrack(comb_arr, op, cl+1)
                comb_arr.pop()
        backtrack([], 0, 0)
        return res