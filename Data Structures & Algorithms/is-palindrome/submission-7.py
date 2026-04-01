class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Remvoe all spaces
        s.replace(" ", "")
        
        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            #if any of the letters are not alphanumeric
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True

        