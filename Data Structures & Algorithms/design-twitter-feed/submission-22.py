import collections
class Twitter:

    def __init__(self):
        self.time = 0
        #UserId = set(following)
        self.followMap = defaultdict(set)
        #UserId = [(time, tweet)]
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        res = []
        heap = []

        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                idx = len(self.tweetMap[user]) - 1
                time,tweet = self.tweetMap[user][idx]
                heapq.heappush(heap, (time, tweet, idx, user))
        
        while len(res) < 10 and heap:
            time, tweet, idx, user = heapq.heappop(heap)
            res.append(tweet)

            if idx > 0:
                idx = idx - 1
                time,tweet = self.tweetMap[user][idx]
                heapq.heappush(heap, (time, tweet, idx, user))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
