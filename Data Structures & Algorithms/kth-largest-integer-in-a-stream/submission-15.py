import collections
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        heapq.heapify(self.stream)

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        

        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        
        return self.stream[0]
        
