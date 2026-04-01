class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        nums.sort()

        def back(i, total):
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(nums):
                return
            
            stack.append(nums[i])
            back(i + 1, total + nums[i])
            stack.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            back(i + 1, total)
        
        back(0,0)
        return res
            

        