class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        stack = []

        words = set(wordDict)

        def backtrack(i):
            if i >= len(s):
                res.append(" ".join(stack))
                return

            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    stack.append(s[i:j+1])
                    backtrack(j + 1)
                    stack.pop()
            
            return
        
        backtrack(0)
        return res
        