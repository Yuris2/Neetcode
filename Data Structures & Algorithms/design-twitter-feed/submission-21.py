import collections
class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.follow(userId, userId)

        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                time, tweetId = self.tweetMap[user][-1]
                idx = len(self.tweetMap[user]) - 1
                heapq.heappush(heap, (time, tweetId, user, idx))
        
        feed = []
        while heap and len(feed) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            feed.append(tweetId)
            idx -= 1

            if idx >= 0:
                time,tweetId = self.tweetMap[user][idx]
                heapq.heappush(heap, (time, tweetId, user, idx))
        
        return feed



        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
