import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #monotonic increasing
        q = deque()
        
        l = r = 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res