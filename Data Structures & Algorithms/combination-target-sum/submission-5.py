class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def back(i, summation):
            if summation == target:
                if len(stack) > 0:
                    res.append(stack.copy())
                return

            if i >= len(nums) or summation > target:
                return
            
            stack.append(nums[i])
            back(i, summation + nums[i])
            stack.pop()
            back(i + 1, summation)
        
        back(0,0)
        return res

            
                
            

        