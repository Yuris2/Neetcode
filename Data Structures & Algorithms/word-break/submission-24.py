class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}

        def dp(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            res = False
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = dp(j + 1)
                    if res:
                        cache[i] = True
                        return True
            
            cache[i] = res
            return res
        
        return dp(0)
            

        