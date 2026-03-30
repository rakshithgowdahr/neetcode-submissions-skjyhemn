class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][0]:
                stack.append([temp, i])
                continue
            while stack and temp > stack[-1][0]:
                tmp, index = stack.pop()
                output[index] = i-index
            stack.append([temp, i])
        return output
