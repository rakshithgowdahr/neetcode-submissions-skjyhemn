class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        output = 0
        for c in s:
            counter[c] += 1
            if counter[c] == 2:
                output += 2
                del counter[c]
        return output if not counter else output+1
