class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = [-1] * (len(s) + 1)

        def dp(i):
            if i >= len(s):
                return True
            if cache[i] != -1:
                return bool(cache[i])
            
            for j in range(i,len(s)):
                if s[i:j + 1] in words:
                    if dp(j + 1):
                        cache[i] = 1
                        return True
            
            cache[i] = 0
            return False
        
        return dp(0)
        