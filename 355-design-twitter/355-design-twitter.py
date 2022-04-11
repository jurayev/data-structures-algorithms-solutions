class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        
        hashtable: userid -> tweets(list)
                   1: [10 9 7]
                   2: [8 5 2 1]
        
        hashtable followerid -> followeeid (hash set)
                   1: {2}
        
        """
        self.tweets = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)
        self.timestamp = 0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        O(1)
        """
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        O(n log n)
        """
        news_feed = []
        followees = self.followees[userId]
        followees.add(userId)
        for followee_id in followees:
            followee_tweets = self.tweets[followee_id][-10:]
            news_feed = news_feed + followee_tweets
        return [tweet_id for _, tweet_id in heapq.nlargest(10,news_feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        O(1)
        """
        if followerId == followeeId: return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        O(1)
        """
        if followerId == followeeId: return
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)