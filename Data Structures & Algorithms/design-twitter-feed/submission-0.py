import collections

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        #To include themselves in their own feed
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if user in self.tweetMap:
                index = len(self.tweetMap[user]) - 1
                count, tweetId = self.tweetMap[user][index]
                heapq.heappush(heap,[count, tweetId,index - 1, user])
        
        while heap and len(res) < 10:
            if heap:
                count, tweetId, index, user = heapq.heappop(heap)
                res.append(tweetId)

                if index >= 0:
                    count, tweetId = self.tweetMap[user][index]
                    heapq.heappush(heap, [count, tweetId, index - 1, user])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
