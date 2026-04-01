class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def backtrack(i):
            #BC
            if i >= len(nums):
                res.append(stack.copy())
                return
            #include our result, go down that decision tree
            stack.append(nums[i])
            backtrack(i + 1)
            #exclude our resutl, go down that decision tree
            stack.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
        