class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        store = "abcdefghijklmnopqrstuvwxyz0123456789"
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] not in store:
                i += 1
                continue
            if s[j] not in store:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        