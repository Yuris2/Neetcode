import collections
class MedianFinder:

    def __init__(self):
        #Max heap to store lower half of elements
        self.left = []
        #Min heap to store upper half of elements
        self.right = []
        

    def addNum(self, num: int) -> None:
        #Push into the max heap
        heapq.heappush(self.left, -num)
        #Remove the top value from the max heap
        maxLeft = -heapq.heappop(self.left)
        heapq.heappush(self.right, maxLeft)
        #If the length of the min-heap > max-heap
        if len(self.right) > len(self.left):
            minRight = heapq.heappop(self.right)
            #Pop smallest value from min-heap and add to max heap
            heapq.heappush(self.left, -minRight)
        

    def findMedian(self) -> float:
        #If the length of the min-heap < max-heap:
        if len(self.right) < len(self.left):
            #Return top of max-heap
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0
        #Return top of max_heap and top of min-heap / 2.0
        
        