class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        def char_index(c: str) -> int:
            if 'A' <= c <= 'Z':
                return ord(c) - ord('A')
            if 'a' <= c <= 'z':
                return 26 + ord(c) - ord('a')
            raise ValueError(f"Unsupported character: {c}")
        t_key = [0] * 52
        s_key = [0] * 52
        for c in t:
            t_key[char_index(c)] = t_key[char_index(c)]+1
        def isWindowValid() -> bool:
            for i,c in enumerate(t_key):
                if s_key[i] < c:
                    return False
            return True
        l = r = 0
        min_window_str = ""
        for r in range(len(s)):
            if s[r] in t:
                s_key[char_index(s[r])] = s_key[char_index(s[r])]+1
            while isWindowValid() and l <= r:
                if len(min_window_str) == 0:
                    min_window_str = s[l:r+1]
                min_window_str = s[l:r+1] if len(s[l:r+1]) < len(min_window_str) else min_window_str
                if s[l] in t:
                    s_key[char_index(s[l])] = s_key[char_index(s[l])]-1
                l += 1
        return min_window_str