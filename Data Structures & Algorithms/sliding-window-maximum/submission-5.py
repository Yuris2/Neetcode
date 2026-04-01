import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        L = 0
        R = 0

        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            #If out of bounds
            if L > q[0]:
                q.popleft()
            
            if (R - L + 1) == k:
                res.append(nums[q[0]])
                L += 1
            
            R += 1
        
        return res
        