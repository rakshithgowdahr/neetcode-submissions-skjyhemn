class Twitter:

    def __init__(self):
        self.users = {}
        self.network = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        if userId not in self.users:
            self.users[userId] = {"tweets": []}
        self.users[userId]["tweets"].append([tweetId, self.timer])

    def getNewsFeed(self, userId: int) -> List[int]:
        users = []
        if userId in self.network:
            for user in self.network[userId]:
                users.append(user)
        users.append(userId)
        feed_tweets = []
        all_tweets = []
        for user in users:
            if user in self.users:
                for tweet in self.users[user]["tweets"]:
                    all_tweets.append(tweet)
        feed_tweets = [item[0] for item in sorted(all_tweets, key=lambda x: x[1], reverse=True)]
        return feed_tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = {"tweets": []}
        if followeeId not in self.users:
            self.users[followeeId] = {"tweets": []}
        if followerId not in self.network:
            self.network[followerId] = set()
        self.network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.network:
            if followeeId in  self.network[followerId]:
                self.network[followerId].remove(followeeId)
