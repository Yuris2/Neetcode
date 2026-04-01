class Solution:
    def numDecodings(self, s: str) -> int:
        valid = {'0', '1', '2', '3', '4', '5', '6'}
        cache = {}
        def dp(i):
            #If we have found a valid decoding
            if i >= len(s):
                return 1
            #If we hit a leading 0
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]
            
            res = dp(i + 1)

            if i < len(s) - 1 and (s[i] == '1' or 
            s[i] == '2' and s[i+1] in valid):
                res += dp(i + 2)
            
            cache[i] = res
            return res
        
        return dp(0)
        