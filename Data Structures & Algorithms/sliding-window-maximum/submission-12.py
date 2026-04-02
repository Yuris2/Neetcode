import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #Decreasing queue (index of num)
        q = deque()

        l = r = 0
        while r < len(nums):
            #Maintaining invariant
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            #If out of our window range
            if q[0] < l:
                q.popleft()

            #If our window size is k
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res

        