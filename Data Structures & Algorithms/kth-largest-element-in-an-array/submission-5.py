import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev = [-n for n in nums]
        heapq.heapify(rev)

        for _ in range(k - 1):
            heapq.heappop(rev)
        
        return -rev[0]
        