class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def back(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]
            
            res = 0
            #Decision 1, there is going to be a digit 1-9 
            res += (back(i + 1))
            #Decision 2, check for double digits
            if i < len(s) - 1 and (
                s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7)
            ):
                res += (back(i + 2))
            
            cache[i] = res
            return res
        
        return back(0)
        