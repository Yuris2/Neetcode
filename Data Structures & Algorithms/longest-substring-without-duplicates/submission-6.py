class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            lengthOfWindow = r - l + 1
            res = max(res,lengthOfWindow)
        
        return res
        #Expand the window
        #Check if there are duplicate characters in the substring
        #If there are:
            #Shrink the left side of the window
        #Else:
            #Check if the length of the current window is greater than res
        
        #Run until window hits out of bounds
        