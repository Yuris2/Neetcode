import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        #idx
        q = deque()

        #We have the top of the queue store the greatest value
        #but we need to use the index to see if it is out of bounds
        #Monotonic decreasing queue
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            while q[0] < l:
                q.popleft()
            
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
        
        return res

            

        