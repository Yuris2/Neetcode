class Solution:
    def numDecodings(self, s: str) -> int:
        #No Leading 0's
        valid = {'0','1','2','3','4', '5', '6'}
        cache = {}

        def dp(i):
            if i >= len(s):
                return 1
            if i in cache:
                return cache[i]
            
            if s[i] == '0':
                return 0
            
            res = dp(i + 1)

            if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in valid)):
                res += dp(i + 2)
            
            cache[i] = res
            return res
        
        return dp(0)