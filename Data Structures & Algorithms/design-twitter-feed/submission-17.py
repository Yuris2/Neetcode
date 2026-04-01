import collections
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.time))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        self.follow(userId, userId)
        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                tweetId, time = self.tweetMap[user][index]
                heapq.heappush(heap, (time, tweetId, user, index))
        
        while heap and len(feed) < 10:
            time, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                index = index - 1
                tweetId, time = self.tweetMap[user][index]
                heapq.heappush(heap, (time, tweetId, user, index))
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
