class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Pattern
            #2D-DP with 3 choices and decisions for both dimensions
        
        #General Idea
            #If you run out of chars in w1 or w2, return remaining in other word
            #If chars are equal, move to next letter
            #Else, return min(insertion, deletion, replacement)
            #dp[i][j] = min operations to transform w1[:i] and w2[:j]
        
        #Pseudocode (Recursive) - track i, j
            #BC: when i == len(w1) and j == len(word2):
                #Return 0
            
            #If we have equal chars at w1[i] and w2[j]:
                #Go to the next letter
            #Else:
                #c1 = Try removing a letter
                #c2 = Try adding a letter

                #Return the min of c1,c2
        
        n,m = len(word1), len(word2)

        dp = [[2e9] * (m + 1) for _ in range(n + 1)]

        #Filling in the base case (i == n)
        for j in range(m + 1):
            dp[n][j] = m - j
        
        #(j == m) no more characters in w2
        for i in range(n + 1):
            dp[i][m] = n -i

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
                    dp[i][j] = min(dp[i + 1][j + 1], dp[i][j])
                    dp[i][j] += 1
        
        return dp[0][0]
                
            
        