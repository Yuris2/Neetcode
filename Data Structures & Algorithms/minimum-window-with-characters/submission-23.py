import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Pattern
            #Sliding Window with Hashmap
        
        #Idea
            #Use a sliding window to find 
            #min substring where have == need
            #have = count(char[s]) == count(char{t})
            #need = len(countT)
        
        #Initialize two pointers
        l = 0
        #Count the characters of t 
        countT = Counter(t)
        countS = defaultdict(int)
        #Track minLength and res
        minLength = 2e9
        res = ""
        #Approach fails when countS has higher frequency
        #Than countT for a certain letter
        have = 0
        need = len(countT)

        #Slide l and r pointer across the window
        for r,c in enumerate(s):
            #If r is in the count of t:
            if c in countT:
                #Add count to s
                countS[c] += 1

                if countS[c] == countT[c]:
                    have += 1
                

            #While the counts are equal
            while have == need:
                #Compare length to minLength: 
                if (r - l + 1) < minLength:
                    #Update if less
                    minLength = r - l + 1
                    res = s[l:r+1]
                #Slide left window over by one
                
                #If char in count of T:
                if s[l] in countT:
                     #Decrement 
                    countS[s[l]] -= 1

                if countS[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        return res
                
                   
        
        #Return res

        