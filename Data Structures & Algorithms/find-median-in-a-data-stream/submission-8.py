import heapq
class MedianFinder:

    def __init__(self):
        #Max Heap
        self.left = []
        #Min Heap
        self.right = []
        

    def addNum(self, num: int) -> None:
        #Push on the left heap
        heapq.heappush(self.left, -num)
        #Extract the largest number from the left heap
        maxLeft = -heapq.heappop(self.left)
        #Add to the right heap
        heapq.heappush(self.right, maxLeft)
        #We want the left heap to hold more values
        if len(self.left) < len(self.right):
            minRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -minRight)
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
        
        