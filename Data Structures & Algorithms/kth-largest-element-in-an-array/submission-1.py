import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Approach.
        #1. turn array into a max heap
        #2. pop k elements from the array
        #3. return kth element

        elem = None
        #1.
        nums = [-n for n in nums]
        heapq.heapify(nums)
        #2, 3
        while k > 0:
            elem = heapq.heappop(nums)
            k -= 1
        
        #REMEMBER TAKE NEGATIVE
        return -elem

        