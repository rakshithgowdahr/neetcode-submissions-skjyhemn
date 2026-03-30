class Twitter:

    def __init__(self):
        self.clock = 0
        self.tweets = defaultdict(list)
        self.network = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.clock, tweetId])
        self.clock -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        self.network[userId].add(userId)
        for followeeId in self.network[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                clock, tweetId = self.tweets[followeeId][index]
                max_heap.append([clock, tweetId, followeeId, index-1])
        heapq.heapify(max_heap)
        while max_heap and len(res) < 10:
            clock, tweetId, followeeId, index = heapq.heappop(max_heap)
            res.append(tweetId)
            if index >= 0:
                clock, tweetId = self.tweets[followeeId][index]
                heapq.heappush(max_heap, [clock, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].discard(followeeId)
