import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l = r = 0

        while r < len(nums):
            #Maintain decreasing stack
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #If the window is too large
            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
