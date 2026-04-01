import heapq
class MedianFinder:

    def __init__(self):
        self.maxLeft = []
        self.minRight = []
        
    def addNum(self, num: int) -> None:
        #Add number into the left maxHeap
        heapq.heappush(self.maxLeft, -num)
        #Pop the largest value from the maxHeap into the minHeap
        leftVal = -heapq.heappop(self.maxLeft)
        heapq.heappush(self.minRight, leftVal)
        #Move the smallest value from the minHeap to max if min > max
        if len(self.minRight) > len(self.maxLeft):
            rightVal = heapq.heappop(self.minRight)
            heapq.heappush(self.maxLeft, -rightVal)
        
    def findMedian(self) -> float:
        if len(self.maxLeft) > len(self.minRight):
            return -self.maxLeft[0]
        return (-self.maxLeft[0] + self.minRight[0]) / 2.0
        
        
        