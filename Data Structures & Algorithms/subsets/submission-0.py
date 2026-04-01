class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            #1, 2, 3 = > 2
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        

        backtrack(0)
        return res
        