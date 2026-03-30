class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                first = int(stack.pop())
                second = int(stack.pop())
                output = 0
                if token == "+":
                    output = first + second
                elif token == "-":
                    output = second - first
                elif token == "*":
                    output = first * second
                else:
                    output = second / first
                stack.append(output)
            else:
                stack.append(token)
        return int(stack[0]) if len(stack) else 0