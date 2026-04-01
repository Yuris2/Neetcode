class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #First have to take the sum of all numbers, // 2
        #If not even, return False
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        cache = {}
        #[1,2,3,4] => 5 => 4
        #Target, 
        #We can decide whether or not to take the number to contr to targer
        #We can keep checking
        #Continue until we get 0, or we return False

        def backtrack(i,target):
            if i >= len(nums):
                if target == 0:
                    return True
                return False
            if (i, target) in cache:
                return cache[(i, target)]
            
            res = (backtrack(i + 1, target - nums[i]) or
            backtrack(i + 1, target)
            )

            cache[(i, target)] = res

            return res
        
        return backtrack(0, totalSum // 2)
        
