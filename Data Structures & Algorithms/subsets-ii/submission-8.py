class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        nums.sort()

        def back(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            back(i + 1)
            stack.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            back(i + 1)
        
        back(0)
        return res
        