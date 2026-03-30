class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hash_set = set()
        adj = defaultdict(list)
        for word in wordList:
            hash_set.add(word)
        if endWord not in hash_set:
            return 0
        hash_set.add(beginWord)
        hash_set.add(endWord)
        for word in wordList: #O(number of words * word length)
            for i in range(len(word)):
                for l in "abcdefghijklmnopqrstuvwxyz":
                    comb_word = word[:i]+l+word[i+1:]
                    if comb_word in hash_set and word != comb_word:
                        adj[word].append(comb_word)
        q = deque()
        for word in adj[endWord]:
            q.append((word, None, 1))
        # print(q)
        visited = set()
        while q:
            word, prev, dist = q.popleft()
            if word in visited:
                continue
            visited.add(word)
            if word == beginWord:
                return dist+1
            for nei in adj[word]:
                if nei == prev:
                    continue
                q.append((nei, word, dist+1))
        return 0