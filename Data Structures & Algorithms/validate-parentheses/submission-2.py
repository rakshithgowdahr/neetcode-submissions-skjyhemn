class Solution:
    def isValid(self, s: str) -> bool:
        #(())()
        #()()
        #([]{}){}
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                _c = stack.pop()
                if _c == "[" and c != "]":
                    return False
                if _c == "(" and c != ")":
                    return False
                if _c == "{" and c != "}":
                    return False
        return False if len(stack) else True