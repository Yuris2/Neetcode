class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        
        #[bloo, m]
        # b l o o m b e r g
        #       i
        cache = {}
        def dfs(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    if dfs(j + 1):
                        cache[i] = True
                        return cache[i]
            
            cache[i] = False
            return False

        return dfs(0)
        