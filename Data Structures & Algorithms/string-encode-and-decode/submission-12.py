class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i,string in enumerate(strs):
            encoded_str += (str(len(string))+"#"+string)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            num_str = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                num_str += s[j]
            l = int(num_str)
            i += len(num_str)
            decoded_strs.append(s[i+1:i+l+1])
            i = i+l+1
        return decoded_strs
