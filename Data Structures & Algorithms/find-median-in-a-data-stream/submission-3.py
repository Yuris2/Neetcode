import heapq
class MedianFinder:

    def __init__(self):
        #Max heap
        self.left = []
        #Min Heap
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        maxLeft = -heapq.heappop(self.left)

        #Add maximum element from left into right
        # What happens if we added an extremely large number
        heapq.heappush(self.right, maxLeft)

        #We want the left to hold more elements if odd
        if len(self.right) > len(self.left):
            minRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -minRight)
        

    def findMedian(self) -> float:
        maxLeft = -self.left[0]
        #Odd length
        if len(self.right) < len(self.left):
            return maxLeft
        return (maxLeft + self.right[0]) / 2.0
        
        