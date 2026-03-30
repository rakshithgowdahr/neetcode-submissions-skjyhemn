class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        i, j = 0, len(s)-1
        while i <= j:
            if s[i].lower() not in allowed_chars:
                i += 1
                continue
            if s[j].lower() not in allowed_chars:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            