class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        #Iterate through the array with a sliding window (size k)
        for r in range(len(nums)):
            if (r - l + 1) == k:
                curMax = nums[l]
                for n in range(l, r + 1):
                    curMax = max(curMax, nums[n])
                res.append(curMax)
                l += 1
        
        return res

            #In each window
                #Find the maximum element in that window
                #Append to the result
        