class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dp(i):
            #There is one way to reach the end
            if i >= len(s):
                return 1
            #Can't deal with a zero
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]
            
            res = dp(i + 1)
            if i < len(s) - 1 and (
                s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7)):
                res += dp(i + 2)
            
            cache[i] = res
            return res
        
        return dp(0)
        