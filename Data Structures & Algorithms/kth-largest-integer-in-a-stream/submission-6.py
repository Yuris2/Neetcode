import collections

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        self.limit = k

        while len(self.nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.limit:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
