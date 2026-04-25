class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        output = ""
        while i < len(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or i >= len(strs[j-1]) or strs[j][i] != strs[j-1][i]:
                    return output
            output += strs[0][i]
            i += 1
        return output