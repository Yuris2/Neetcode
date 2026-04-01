class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def back(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            back(i + 1)
            stack.pop()
            back(i + 1)
        
        back(0)
        return res
        