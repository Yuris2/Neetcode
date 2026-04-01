class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charWindow = set()
        #Ensure that in the current window there are no duplicate characters
        #If there is a duplicate character, shrink the left side of the window until there are no more duplicates
        #Move the right side of window forward
        #Keep going until string hits the end of the window

        l = 0

        for r in range(len(s)):
            while s[r] in charWindow:
                charWindow.remove(s[l])
                l += 1
            
            charWindow.add(s[r])

            res = max(res, r - l + 1)
        
        return res

        