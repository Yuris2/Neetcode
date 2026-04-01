class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def back():
            if len(stack) == len(nums):
                res.append(stack.copy())
                return
            
            for n in nums:
                if n not in stack:
                    stack.append(n)
                    back()
                    stack.pop()
        
        back()
        return res
        