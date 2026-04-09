class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Given two strings, return the length of the longest subsequence
        #Return 0 if there are none
        cache = {}

        #Solution Intuition
        def dp(i,j):
            #If we are out of letters
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = 0
            #If we have a letter match
            if text1[i] == text2[j]:
                res += 1 + dp(i + 1, j + 1)
            #Try moving pointer for both words
            else:
                move1 = dp(i + 1, j)
                move2 = dp(i, j + 1)

                res = max(move1, move2)
            
            cache[(i,j)] = res
            return res
        
        return dp(0,0)
        