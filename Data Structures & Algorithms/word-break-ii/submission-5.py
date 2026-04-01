class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        stack = []
        words = set(wordDict)

        def dfs(i):
            if i >= len(s):
                res.append(" ".join(stack))
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    stack.append(s[i:j+1])
                    dfs(j + 1)
                    stack.pop()
            
            return 
        
        dfs(0)
        return res