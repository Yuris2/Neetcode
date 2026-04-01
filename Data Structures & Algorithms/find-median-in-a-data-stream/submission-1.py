import heapq
class MedianFinder:
    def __init__(self):
        #Max heap
        self.small = []
        #Min heap
        self.large = []
        
    def addNum(self, num: int) -> None:
        #Push onto the small heap
        heapq.heappush(self.small, -num)
        #Push the max of the small heap onto the large
        maxSmall = -heapq.heappop(self.small)
        heapq.heappush(self.large, maxSmall)
        #Rebalance heap. Think if we pushed 1 million 
        if len(self.large) > len(self.small):
            minLarge = heapq.heappop(self.large)
            heapq.heappush(self.small, -minLarge)
        
    def findMedian(self) -> float:
        #Small heap guaranteed to have more elements.
        #Odd if small heap has more
        if len(self.small) > len(self.large):
            return -self.small[0]
        #Even parity
        median = ((-self.small[0]) + (self.large[0])) / 2.0
        return median
        
        