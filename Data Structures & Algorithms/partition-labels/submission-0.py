class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #xyxxyzbz -> xyxxy, zbz
        # {x:3, y:4, z:7}
        hash_map = defaultdict(int)
        for i in range(len(s)):
            hash_map[s[i]] = i
        output = []
        curr_char = s[0]
        prev_index = 0
        for i in range(len(s)):
            if i == hash_map[curr_char]:
                output.append((i+1)-prev_index)
                curr_char = s[i+1] if i+1 < len(s) else ""
                prev_index = i+1
                continue
            if s[i] != curr_char:
                curr_char = s[i] if hash_map[s[i]] > hash_map[curr_char] else curr_char
        return output