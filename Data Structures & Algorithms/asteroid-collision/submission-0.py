class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #[5, 10, -5, -6] -> [5, 10, -6] -> [5, 10]
        stack = []
        for i, ast in enumerate(asteroids):
            stack.append(ast)
            while len(stack) > 1 and (stack[-1] < 0 and stack[-2] > 0):
                ast1 = stack.pop()
                ast2 = stack.pop()
                if abs(ast1) == abs(ast2):
                    continue
                if abs(ast1) > abs(ast2):
                    stack.append(ast1)
                else:
                    stack.append(ast2)
        return stack