class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}

        #Seeing last occ
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        #Tracking max jump
        far = 0
        end = 0
        #Iterating through the string
        for i in range(len(s)):
            #See the last index of char
            far = max(far, lastIndex[s[i]])

            if far == i:
                res.append(far - end + 1)
                end = i + 1
        
        return res
        