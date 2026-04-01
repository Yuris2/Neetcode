class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #Fixed Sliding Window of length k
        #Can k be larger than nums
        #Store into an array

        prevMax = -2e9
        #How we would solve it as a human
        l = 0
        #Start with this window at position 0 and grow until size == k
        for r in range(k - 1, len(nums)):
            window = nums[l:r+1]
            res.append(max(window))
        #Find the maximum element and then append to the res
        #Grow the window from the right and shrink from left
            #Check if maximum has been removed
            #Compare maximum with new number added
            l += 1
        return res
        #Return res

        