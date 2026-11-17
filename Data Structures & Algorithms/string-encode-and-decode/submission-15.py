class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in range(len(strs)):
            encoded_str += (str(len(strs[i]))+"#"+strs[i])
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        c_num = ''
        while i < len(s):
            if s[i] == "#":
                i += 1
                c_num = int(c_num)
                decoded_strs.append(s[i:i+c_num])
                i += c_num
                c_num = ''
                continue
            c_num += s[i]
            i += 1
        return decoded_strs