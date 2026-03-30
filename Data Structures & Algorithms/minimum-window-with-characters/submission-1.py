class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = dict()
        window_map = defaultdict(int)
        def validWindow():
            for key in t_map:
                if key not in window_map or window_map[key] < t_map[key]:
                    return False
            return True
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        l = 0
        output_str = None
        for r in range(len(s)):
            window_map[s[r]] += 1
            while validWindow():
                if output_str == None:
                    output_str = s[l:r+1]
                else:
                    output_str = s[l:r+1] if r-l+1 <= len(output_str) else output_str
                if s[l] in window_map: 
                    window_map[s[l]] -= 1
                    if window_map[s[l]] < 1:
                        del window_map[s[l]]
                l += 1
        return output_str if output_str else ""