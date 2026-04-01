import collections
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.page = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.page))
        self.page -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        self.follow(userId, userId)
        #All users the user follows
        for user in self.followMap[userId]:
            #If the user has even tweeted
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                tweetId, time = self.tweetMap[user][index]
                #Time is to sort, index is to see when the user
                #used all of their tweets
                heapq.heappush(heap,(time, tweetId, user, index))
        
        while heap and len(feed) < 10:
            time, tweet, user, index = heapq.heappop(heap)
            feed.append(tweet)

            if index > 0:
                index -= 1
                newTweet, newTime = self.tweetMap[user][index]
                heapq.heappush(heap, (newTime, newTweet, user, index))
        
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
