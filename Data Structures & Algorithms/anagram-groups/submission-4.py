class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c)-ord("a")] += 1
            hash_map[tuple(key)].append(word)
        output = []
        for key in hash_map.keys():
            output.append(hash_map[key])
        return output