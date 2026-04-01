import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #Represents the max element/index in our window
        #Not the number because we can have duplicates
        #Decreasing sequence because we want to have max candidate in a range
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #If our max candidate expired
            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
        