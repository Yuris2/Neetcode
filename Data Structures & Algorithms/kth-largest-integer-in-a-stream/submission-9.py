import collections

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.elems = nums
        self.k = k
        heapq.heapify(self.elems)
        while len(self.elems) > self.k:
            heapq.heappop(self.elems)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.elems, val)

        while len(self.elems) > self.k:
            heapq.heappop(self.elems)
        
        return self.elems[0]
        

        
