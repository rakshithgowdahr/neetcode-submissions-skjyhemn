class Solution:
    def longestPalindrome(self, s: str) -> str:
        output_s = ""
        def traverse(i):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            s1 = s[l+1:r]
            s2 = ""
            if(i+1 < len(s) and s[i] == s[i+1]):
                l, r = i, i+1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        l-=1
                        r+=1
                    else:
                        break
                s2 = s[l+1:r]
            return s2 if len(s2) >= len(s1) else s1
        for i in range(len(s)):
            _s = traverse(i)
            if(len(_s) >= len(output_s)):
                output_s = _s
        return output_s