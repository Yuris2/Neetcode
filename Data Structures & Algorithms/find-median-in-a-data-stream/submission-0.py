import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, x: int) -> None:
        # 1) push to small
        heapq.heappush(self.small, -x)
        # 2) move the largest of small to large -> enforces order invariant
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 3) rebalance sizes so small can hold the extra when odd
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
