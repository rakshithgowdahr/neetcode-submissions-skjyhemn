class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        hash_map = dict()
        for i, num in enumerate(nums2):
            hash_map[num] = i
        m_stack = [[0, nums2[0]]]
        arr2 = [-1] * len(nums2)
        for i in range(1, len(nums2)):
            while m_stack and m_stack[-1][1] < nums2[i]:
                index, num = m_stack.pop()
                arr2[index] = nums2[i]
            m_stack.append([i, nums2[i]])
        for i, num in enumerate(nums1):
            output[i] = arr2[hash_map[num]]
        return output
        