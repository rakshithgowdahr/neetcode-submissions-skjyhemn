class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m_stack = [[0, temperatures[0]]]
        output = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while m_stack and m_stack[-1][1] < temperatures[i]:
                index, temp = m_stack.pop()
                output[index] = i-index
            m_stack.append([i, temperatures[i]])
        return output

