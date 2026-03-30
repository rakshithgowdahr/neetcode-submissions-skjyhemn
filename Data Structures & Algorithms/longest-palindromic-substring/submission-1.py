class Solution:
    def longestPalindrome(self, s: str) -> str:
        #xyzaa
        #ababd
        #habbah
        n = len(s)
        longest_palindrome = s[0]
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                longest_palindrome = s[l:r+1] if len(s[l:r+1]) > len(longest_palindrome) else longest_palindrome
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                longest_palindrome = s[l:r+1] if len(s[l:r+1]) > len(longest_palindrome) else longest_palindrome
                l -= 1
                r += 1
        return longest_palindrome

