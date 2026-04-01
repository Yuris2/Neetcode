import collections
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.page = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.page))
        self.page -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                tweet, time = self.tweetMap[user][index]
                heapq.heappush(heap, (time, tweet, index, user))
        
        while heap and len(feed) < 10:
            time, tweet, index, user = heapq.heappop(heap)
            feed.append(tweet)

            if index > 0:
                index = index - 1
                newTweet, newTime = self.tweetMap[user][index]
                heapq.heappush(heap, (newTime, newTweet, index, user))
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
