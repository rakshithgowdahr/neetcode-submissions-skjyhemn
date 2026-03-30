class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += (str(len(s))+"#"+s)
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            for c in range(i, len(s)):
                if s[c] == "#":
                    break
                j += 1
            word_len = int(s[i:j])
            if word_len == 0:
                output.append("")
            else:
                output.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return output
        
