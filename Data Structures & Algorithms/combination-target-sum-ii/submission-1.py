class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        #Remove dupes
        nums.sort()

        #Choice 1 = Include number
        #Choice 2 = Don't Include Number
            #Can't include a previously included number
        def back(i, total):
            #if we have reached our target
            if total == target:
                #add the combination to our res
                res.append(stack.copy())
                return
            
            #if we have exhausted each of our numbers
            if i >= len(nums):
                return
            
            #add the current number
            stack.append(nums[i])
            #go down rabbit hole
            back(i + 1, total + nums[i])
            #remove number
            stack.pop()
            #Skip over duplicate numbers
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            #make other choice
            back(i + 1, total)
        
        back(0,0)
        return res

        