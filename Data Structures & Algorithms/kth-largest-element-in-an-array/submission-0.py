import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        elem = None
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            elem = heapq.heappop(nums)
        

        if elem:
            return -elem
        
        return elem
        
        