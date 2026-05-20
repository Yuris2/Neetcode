class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-n for n in nums]    
        heapq.heapify(res)
        ans = 0

        for i in range(k):
            ans = -heapq.heappop(res)
        
        return ans

        