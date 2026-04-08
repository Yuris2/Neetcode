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
        heap = []
        self.follow(userId, userId)

        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                idx = len(self.tweetMap[user]) - 1
                tweet, time = self.tweetMap[user][idx]
                heapq.heappush(heap, [time, tweet, idx, user])

        res = []
        while heap and len(res) < 10:
            time, tweet, idx, user = heapq.heappop(heap)
            res.append(tweet)

            if idx > 0:
                idx -= 1
                tweet, time = self.tweetMap[user][idx]
                heapq.heappush(heap, [time, tweet, idx, user])  

        return res      

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
