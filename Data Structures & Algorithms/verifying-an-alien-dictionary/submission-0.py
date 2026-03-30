class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        s = ""
        #ag, disk, dog
        #disc, disco
        #disco, disc
        for i in range(len(words)-1):
            j = 0
            while True:
                if j == len(words[i]) or j == len(words[i+1]):
                    if len(words[i]) > len(words[i+1]):
                        return False
                    break
                if words[i][j] == words[i+1][j]:
                    j += 1
                    continue
                if order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False
                break
        return True