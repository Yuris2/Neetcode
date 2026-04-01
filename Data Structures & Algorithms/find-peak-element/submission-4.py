class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #[1,3,2,2]
        #[1,1,2,1]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if m - 1 >= 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m + 1 < len(nums) and nums[m] < nums[m + 1]:
                l = m + 1 
            else:
                return m
        
        return -1
            


            
        