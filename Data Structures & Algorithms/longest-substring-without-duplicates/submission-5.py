class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Approach
        #1.     Create a way to manage what char in substring
        #2.     Use pointers to determine the length of a substring
        #3.     Continue until whole string is traversed
        
        window = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])

            res = max(res, r - l + 1)

            r += 1
        
        return res




        