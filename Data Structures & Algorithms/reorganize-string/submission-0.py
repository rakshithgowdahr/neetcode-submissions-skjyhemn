class Solution:
    def reorganizeString(self, s: str) -> str:
        #{a:1, x:1, y:2}
        #{a:1, b:2, c:2, d:2} -> bcdabcd
        #{a:1, b:3, c:2}
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        output = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            output += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return output