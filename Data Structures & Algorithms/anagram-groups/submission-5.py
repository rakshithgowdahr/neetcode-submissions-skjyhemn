class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[tuple(sorted(s))].append(s)
        output = []
        for key in hash_map.keys():
            output.append(hash_map[key])
        return output