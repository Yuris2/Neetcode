class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        level = []
        words = set(wordDict)

        def dfs(i):
            if i >= len(s):
                res.append(" ".join(level))
                return

            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    level.append(s[i:j+1])
                    dfs(j + 1)
                    level.pop()

        dfs(0)
        return res

        