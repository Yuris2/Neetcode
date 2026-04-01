class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #[2,5,6,9] 
        #[2,2,5], [2,5,2]
        res = []
        stack = []
        '''
                    /\
                [2].  []
               /   \. 
             [2,2] [2]
                    /
                  [2,5]
            /
        [2,2,2]
        '''

        def backtrack(i, total):
            if total == target:
                res.append(stack.copy())
                return

            if i >= len(nums) or total > target:
                return
            #1. Do we include the current number into our path/sum
            stack.append(nums[i])
            backtrack(i, total + nums[i])
            #2. Do we want to keep checking the other numbers
            stack.pop()
            backtrack(i + 1, total)
        
            return
        
        backtrack(0, 0)
        return res
    
        