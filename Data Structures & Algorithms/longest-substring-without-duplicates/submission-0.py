class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        #Sliding window approach
        left = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[r])
            res = max(res, r - left + 1)
        
        return res