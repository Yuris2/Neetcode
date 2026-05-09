class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #Determine the unique ways to generate string t by 
        #splitting s into various subsequences
        cache = {}

    #Brute Force
        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
  
            res = 0
            #If s[i] == t[j]:
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            
            #Add the result with skipping s[i] (i + 1, j)
            res += dp(i + 1, j)
            cache[(i,j)] = res

            return res
        
        return dp(0,0)
            


        