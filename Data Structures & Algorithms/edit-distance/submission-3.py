class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Pattern
            #2D-DP with 3 choices and decisions for both dimensions
        
        #General Idea
        
        #Pseudocode (Recursive) - track i, j
            #BC: when i == len(w1) and j == len(word2):
                #Return 0
            
            #If we have equal chars at w1[i] and w2[j]:
                #Go to the next letter
            #Else:
                #c1 = Try removing a letter
                #c2 = Try adding a letter

                #Return the min of c1,c2
        
        cache = {}
        n,m = len(word1), len(word2)
        def dp(i,j):
            #If we hit the end of word 1
            if i == n:
                #Return the remaining chars of m
                return m - j
            if j == m:
                #Return the remaining chars of n
                return n - i
            if (i,j) in cache:
                return cache[(i,j)]
            
            if word1[i] == word2[j]:
                cache[(i,j)] = dp(i + 1, j + 1)
            else:
                #Delete
                c1 = 1 + dp(i + 1, j)
                #Insert
                c2 = 1 + dp(i, j + 1)
                #Replace
                c3 = 1 + dp(i + 1, j + 1)

                cache[(i,j)] = min(c1, c2, c3)
            
            return cache[(i,j)]
        
        return dp(0,0)
            
        