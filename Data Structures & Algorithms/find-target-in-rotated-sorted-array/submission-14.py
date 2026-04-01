class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        #Find the minimum
        while l < r:
            m = (l + r) // 2
            
            #The number in the middle is def not the min
            if nums[m] < nums[r]:
                r = m
            #The number in the middle count be the min
            else:
                l = m + 1
        
        #r holds in the index of the min number
        if target <= nums[-1] and target >= nums[r]:
            l,r = r, len(nums) - 1
        elif target >= nums[0] and target >= nums[r]:
            l,r = 0, r - 1 
        else:
            l,r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1        