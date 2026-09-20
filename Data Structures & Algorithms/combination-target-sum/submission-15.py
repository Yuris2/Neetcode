class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def back(i,summ):
            if summ == target:
                res.append(stack.copy())
                return
            if summ >= target or i >= len(nums):
                return
            
            stack.append(nums[i])
            back(i, summ + nums[i])
            stack.pop()
            back(i + 1, summ)
        
        back(0,0)
        return res