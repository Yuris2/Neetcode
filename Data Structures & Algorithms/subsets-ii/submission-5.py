class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        stack = []

        def back(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            back(i + 1)
            stack.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            back(i + 1)
        
        back(0)
        return res
        