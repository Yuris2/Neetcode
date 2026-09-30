class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #Want to find the max product, 
        res = -2e9
        #Notes
        #Kandane's (with Products)
            #-We can grow/shrink the window based on the running product
            #-We should track both the minimum/maximum product in a given subwindow
        
        #min,max = -10,2
        #[1,2,-5,-5,10]
        minP, maxP = 1,1
        res = -2e9

        for n in nums:
            temp = maxP
            maxP = max(n, maxP * n, minP * n)
            minP = min(n, minP * n, temp * n)

            res = max(res, maxP)
        
        return res


        #3 options
            #Multiply * n
            #Multiple by opp * n
            #Set to n
        
        

        