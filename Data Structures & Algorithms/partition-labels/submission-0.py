class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Maximize number of substrings
        res = []
        lastIndex = {}
        
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        start = 0
        far = 0
        #Iterate through the string tracking i and far_point, start
        for i, c in enumerate(s):
            #set far_point = max(far_point, lastIndex[character])            
            far = max(far, lastIndex[c])
            #If far_point = currentIndex, we have encapsulated within a substring
            if i == far:
                #Append result
                res.append((i - start + 1))
                #Start a new substring length
                start = i + 1
        
        return res