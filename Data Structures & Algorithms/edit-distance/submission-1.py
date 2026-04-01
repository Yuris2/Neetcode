class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        cache = {}
        def backtrack(i,j):
            #if we run out of charaters in word1
            if i == n:
                #Insert remaining characters from word2
                return m - j
            if j == m:
                #Delete remaining characters from word1
                return n - i
            if (i,j) in cache:
                return cache[(i,j)]
            
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:
                #Deleting a char in word1 and inserting a char in word1
                res = min(backtrack(i, j + 1), backtrack(i + 1,j))
                #And replacing a character
                res = min(backtrack(i + 1, j + 1), res)
                res += 1
                cache[(i,j)] = res
            
            return res
        
        return backtrack(0,0)

        