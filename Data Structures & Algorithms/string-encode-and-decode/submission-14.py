class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+"#"+word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            num = ""
            j = i
            while j < len(s):
                if s[j] == '#':
                    break
                num += s[j]
                j += 1
            num = int(num)
            output.append(s[j+1:j+num+1])
            i = j+num+1
        return output