class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def back(i, total):
            if total == target:
                res.append(stack.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            stack.append(nums[i])
            back(i, total + nums[i])
            stack.pop()
            back(i + 1, total)
        
        back(0,0)
        return res

        