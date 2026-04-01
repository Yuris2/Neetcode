class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        cache = {}
        def backtrack(i, total):
            #We have to iterate over each number
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i,total) in cache:
                return cache[(i,total)]
                
            #Choosing to add or subtract
            addChoice = backtrack(i + 1, total + nums[i])
            subChoice = backtrack(i + 1, total - nums[i])

            cache[(i,total)] = addChoice + subChoice
            return cache[(i,total)]

        res += backtrack(0,0)
        return res

        #two choices
        #add to total sum
        #subtract to totalsum
        #We have to use the whole array
        