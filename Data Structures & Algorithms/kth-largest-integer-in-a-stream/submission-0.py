import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.elem = nums
        self.k = k
        heapq.heapify(self.elem)

        while len(self.elem ) > k:
            #pop out the smallest element
            heapq.heappop(self.elem)

        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.elem, val)

        if len(self.elem) > self.k:
            heapq.heappop(self.elem)

        return self.elem[0]
        
