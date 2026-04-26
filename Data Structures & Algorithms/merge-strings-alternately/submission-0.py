class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        output = ""
        while i < len(word1) and i < len(word2):
            output += (word1[i]+word2[i])
            i += 1
        if i < len(word1):
            output += word1[i:]
        if i < len(word2):
            output += word2[i:]
        return output