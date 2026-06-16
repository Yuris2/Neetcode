import collections
class MedianFinder:
    #[1,2,3,4]
    #[1]
    #[2,3,4]

    def __init__(self):
        #Max Heap
        self.left = []
        #Min Heap
        self.right = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        maxLeft = heapq.heappop(self.left)
        heapq.heappush(self.right, -maxLeft)

        if len(self.right) > len(self.left) + 1:
            minRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -minRight)
        
    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (self.right[0] + -self.left[0]) / 2.0
        
        