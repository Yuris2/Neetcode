class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        level = []

        def backtrack():
            if len(level) == len(nums):
                res.append(level.copy())
                return
            
            for n in nums:
                if n not in level:
                    level.append(n)
                    backtrack()
                    level.pop()
        
        backtrack()
        return res

            
        