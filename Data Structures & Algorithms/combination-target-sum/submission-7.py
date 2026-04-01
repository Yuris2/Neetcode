class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def back(i,total):
            if total == target:
                res.append(stack.copy())
                return
            if total > target or i >= len(nums):
                return
             
            stack.append(nums[i])
            back(i, total + nums[i])
            stack.pop()
            back(i + 1, total)
        
        back(0,0)
        return res
            
            
        