class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            
            if nums[m] > nums[l]:
                l = m + 1
            
            else:
                res = min(res, nums[r])
                r = m - 1
        
        return res
            

