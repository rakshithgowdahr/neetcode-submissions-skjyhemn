class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                a2 = stack.pop()
                a1 = stack.pop()
                if token == "+":
                    stack.append((int(a1))+(int(a2)))
                if token == "-":
                    stack.append((int(a1))-(int(a2)))
                if token == "*":
                    stack.append((int(a1))*(int(a2)))
                if token == "/":
                    stack.append((int(a1))/(int(a2)))
            else:
                stack.append(token)
        return int(stack[-1])