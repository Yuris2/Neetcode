import heapq
class MedianFinder:
    def __init__(self):
        #Max Heap
        self.left = []
        #Min Heap
        self.right = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        maxLeft = -heapq.heappop(self.left)

        heapq.heappush(self.right, maxLeft)
        if len(self.right) > len(self.left):
            minRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -minRight)
        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
        
        