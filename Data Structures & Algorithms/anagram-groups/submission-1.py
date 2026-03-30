class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for _str in strs:
            store = [[0, None]] * 26
            for c in _str:
                pos = ord(c) - ord("a")
                store[pos] = [store[pos][0]+1, c]
            key = ""
            for st in store:
                if st[0] == 0 or st[1] == None:
                    continue
                key += str(st[0])+st[1]            
            if key in hash_map:
                hash_map[key].append(_str)
            else:
                hash_map[key] = [_str]
        output = []
        for key in hash_map.keys():
            output.append(hash_map[key])
        return output