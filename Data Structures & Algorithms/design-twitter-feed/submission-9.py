import collections
class Twitter:

    def __init__(self):
        #User ID to people who they follow
        self.followMap = defaultdict(set)
        #User Id => List of Tweets
        self.tweetMap = defaultdict(list)
        #Track the current index (decrement to get most recent)
        self.page = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.page))
        self.page -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        self.followMap[userId].add(userId)
        #Gather each candidate that the userId follows into a list
        for user in self.followMap[userId]:
            #Ensure they even posted a tweet
            if self.tweetMap[user]:
                #Index is most recent element and we are going to go backwards
                index = len(self.tweetMap[user]) - 1
                #Add most recent element on to a heap
                tweetId, time = self.tweetMap[user][index]
                #Had to be sorted by time, not ID
                heapq.heappush(heap, (time, tweetId, user, index))
        #Extract, and replenish the heap
        while heap and len(feed) < 10:
            time, tweet, user, index = heapq.heappop(heap)
            feed.append(tweet)

            if index > 0:
                index = index - 1
                newTweet, newTime = self.tweetMap[user][index]
                heapq.heappush(heap, (newTime, newTweet, user, index))
        #Continue until the length is 10 or we run out of elements
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
