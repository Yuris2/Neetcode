import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stream = nums.copy()
        self.k = k

        heapq.heapify(self.stream)

        while len(self.stream) > k:
            heapq.heappop(self.stream)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        
        return self.stream[0]


        
