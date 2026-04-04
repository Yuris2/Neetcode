class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}

        def dp(i):
            #If we reach the end of the string
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            cache[i] = False
            for j in range(i, len(s)):
                #See if our substring is in words
                if s[i:j+1] in words:
                    #If we can reach the end of the string
                    if dp(j + 1):
                        cache[i] = True

            return cache[i]
        
        return dp(0)
            
