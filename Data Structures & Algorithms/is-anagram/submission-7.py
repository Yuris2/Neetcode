class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        counter = {}
        #Populating counter
        for c in s:
            counter[c] = 1 + counter.get(c,0)
        
        for c in t:
            if c in counter and counter[c] > 0:
                counter[c] -= 1
            else:
                return False
        
        return True
        


        