class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Problem
            #Find the max number of coins you can receive from bursting balloons
            #With the equation. However, size of the array changes as balloons are 
            #popped
        
        #Solution Intuition
            #Pad the arrays with ones to avoid edge cases
            #View the problem as which balloon should we pop last to 
            #get the max value
            #Option(i,j) should represent the max value we get from popping balloons i,j
    

        """
           0,1,2,3
        [1,4,2,3,7,1]
        Recurrence
        op(END) = max(
            1 * 4 * 1 + op(1,3)
            1 * 2 * 1 + op(0,0) + op(2,3)
            1 * 3 * 1 + op(0,1) + op(3,3)
            1 * 7 * 1 + op(0,2)
        )

        op(1,3) = max(
            4 * 2 * 1 + op(2,3)
            4 * 3 * 1 + op(1,1) + op(3,3)
            4 * 7 * 1 + op(1,2)
        )
        """
        
        nums = [1] + nums + [1]
        cache = {}
        def dp(i,j):
            if i > j:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            res = 0
            for k in range(i + 1,j):
                choice = nums[i] * nums[k] * nums[j] + dp(i,k) + dp(k,j)
                res = max(choice, res)
            
            cache[(i,j)] = res
            return res
        
        return dp(0, len(nums) - 1)


        