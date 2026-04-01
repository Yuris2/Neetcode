'''
[3,4,5,6,1,2]
         r
         l

target = 5
[3,4,5,6,1,2]
l       r
[3,4,5,6,1,2]
       
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = 0
        l,r = 0, len(nums) - 1
        #Find where the minimum lies
        while l < r:
            m = (l + r) // 2
        #Check if midpoint > nums[r]
            if nums[m] > nums[r]:
                #Min lies on right of mid
                l = m + 1
            else:
                #midpoint could be min
                r = m
        
        minIndex = r
        minNum = nums[minIndex]

        #Based on where the target lies in retrospect to the min set pointers and B,S
        if minIndex == 0:
            l,r = 0, len(nums) - 1
        elif target > minNum and target > nums[-1]:
            l,r = 0, minIndex - 1
        else:
            l,r = minIndex, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
                    

        