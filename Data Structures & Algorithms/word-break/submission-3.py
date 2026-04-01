class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        res = [False] * (n + 1)
        res[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i:i+len(w)] == w:
                    res[i] = res[i + len(w)]

                    if res[i]:
                        break
        
        return res[0]



        