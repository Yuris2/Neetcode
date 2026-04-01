import heapq

class KthLargest:
    #Approach
    #1.     Initialize an array of nums that is a min heap
    #2.     Keep the heap at length k
    #3.     Value at the end is the kth largest
    #4.     Keep property when adding
    def __init__(self, k: int, nums: List[int]):
        #1.
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        #3.
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
        
