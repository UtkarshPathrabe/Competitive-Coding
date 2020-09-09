class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweetsMap = defaultdict(deque)
        self.followersMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweetsMap[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        maxHeap, newsFeed = [], []
        if len(self.tweetsMap[userId]) > 0:
            time, tweetId = self.tweetsMap[userId][0]
            heappush(maxHeap, (-1 * time, tweetId, userId, 0))
        for follower in self.followersMap[userId]:
            if len(self.tweetsMap[follower]) > 0:
                time, tweetId = self.tweetsMap[follower][0]
                heappush(maxHeap, (-1 * time, tweetId, follower, 0))
        for _ in range(10):
            if not maxHeap:
                break
            time, tweetId, userId, index = heappop(maxHeap)
            newsFeed.append(tweetId)
            if index + 1 < len(self.tweetsMap[userId]):
                time, tweetId = self.tweetsMap[userId][index + 1]
                heappush(maxHeap, (-1 * time, tweetId, userId, index + 1))
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.followersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followersMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)