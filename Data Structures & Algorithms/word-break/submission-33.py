class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}

        def dp(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            for j in range(i,len(s)):
                if s[i:j + 1] in words:
                    if dp(j + 1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return dp(0)
        