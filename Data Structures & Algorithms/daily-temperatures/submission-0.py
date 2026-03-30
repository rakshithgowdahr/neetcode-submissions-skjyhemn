class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append([0, temperatures[0]])
        output = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while len(stack):
                if stack[-1][1] >= temperatures[i]:
                    break
                index, val = stack.pop()
                if val < temperatures[i]:
                    output[index] = i-index
            stack.append([i, temperatures[i]])
        return output