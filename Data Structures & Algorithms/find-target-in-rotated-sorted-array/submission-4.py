class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #First find the min
        minPoint = 0 
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        minPoint = l

        #Find out where to set the pointers
        if minPoint == 0:
            #NORMAL BS
            l, r = 0, len(nums) -1
        elif target >= nums[0]:
            #Left Side of Minpoint
            l, r = 0, minPoint - 1
        else:
            l,r = minPoint, len(nums) - 1
        
        #Regular Binary Search

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1


        