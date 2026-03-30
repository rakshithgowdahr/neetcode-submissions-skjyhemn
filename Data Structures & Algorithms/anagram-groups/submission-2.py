class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for _str in strs:
            bucket = [0] * 26
            for c in _str:
                bucket[ord(c)-ord('a')] += 1
            hash_map[tuple(bucket)].append(_str)
        return [value for value in hash_map.values()]