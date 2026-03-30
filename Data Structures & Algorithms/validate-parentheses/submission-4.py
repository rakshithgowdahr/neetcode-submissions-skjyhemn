class Solution:
    def isValid(self, s: str) -> bool:
        # ()()[()], (()[]){}, (]
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                rm = stack.pop()
                if c == ")" and rm != "(":
                    return False
                if c == "}" and rm != "{":
                    return False
                if c == "]" and rm != "[":
                    return False
        return len(stack) == 0