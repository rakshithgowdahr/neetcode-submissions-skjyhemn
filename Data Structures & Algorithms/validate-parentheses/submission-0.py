class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] in ")]}":
                if len(stack) == 0:
                    return False
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0