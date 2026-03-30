class Solution:
    def isPalindrome(self, s: str) -> bool:
        store = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        i, j = 0, len(s)-1
        while i < j:
            if s[i] not in store:
                i += 1
                continue
            if s[j] not in store:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True