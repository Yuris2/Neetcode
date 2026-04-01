class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        w = set(wordDict)

        res = []
        stack = []

        def dfs(i):
            if i >= n:
                res.append(" ".join(stack))
            
            for j in range(i, n):
                if s[i:j+1] in w:
                    stack.append(s[i:j+1])
                    dfs(j + 1)
                    stack.pop()
            
        
        dfs(0)
        return res
        
        