class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        #Populating a dictionary with count and occurence
        counter = {}
        for c in s:
            counter[c] = 1 + counter.get(c,0)
        
        for c in t:
            if c not in counter or counter[c] <= 0:
                return False
            else:
                counter[c] -= 1
        
        return True

        