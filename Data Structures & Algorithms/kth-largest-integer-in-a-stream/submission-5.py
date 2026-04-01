import collections

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.streams = nums
        self.k = k

        heapq.heapify(self.streams)

        while len(self.streams) > k:
            heapq.heappop(self.streams)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.streams, val)

        if len(self.streams) > self.k:
            heapq.heappop(self.streams)
        
        return self.streams[0]
        
        
        
