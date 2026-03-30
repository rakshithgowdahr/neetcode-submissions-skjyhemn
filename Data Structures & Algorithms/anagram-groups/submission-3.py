class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hash_map = defaultdict(list)
        for s in strs:
            bucket = [0] * 25
            for c in s:
                bucket[ord(c)-ord("a")] += 1
            hash_map[tuple(bucket)].append(s)
        for key in hash_map:
            output.append(hash_map[key])
        return output