class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        #If we sorts the nums array
        nums.sort()
        def backtrack(i):
            if i >= len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()
            #Ensure that next step doesn't equal the same backtrack start that we just ran on
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

            return
        
        backtrack(0)
        return res
        