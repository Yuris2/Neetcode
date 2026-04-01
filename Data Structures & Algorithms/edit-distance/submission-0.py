class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def backtrack(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:
                #minimum between deletion, insetion
                res = min(backtrack(i+1,j), backtrack(i,j+1))
                #minimum between prev and replacing char
                res = min(backtrack(i+1,j+1), res)

                return res + 1
        
        return backtrack(0,0)
        