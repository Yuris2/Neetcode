class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            for j in range(i,len(s)):
                if s[i:j + 1] in wordDict:
                    if dfs(j + 1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return dfs(0)

        