class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        #Letter => Last Occ
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        prevEnd = 0
        far = 0

        for i, c in enumerate(s):
            far = max(far, lastIndex[c])

            if far == i:
                res.append((far - prevEnd + 1))
                prevEnd = i + 1
            
        return res
        