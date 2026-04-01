class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [] 

        def back(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            for n in nums:
                if n not in stack:
                    stack.append(n)
                    back(i + 1)
                    stack.pop()
            

        back(0)
        return res
        