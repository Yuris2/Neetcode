class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i,c in enumerate(s):
            last[c] = i
        
        res = []
        lastIndex = 0
        l = 0

        for r,c in enumerate(s):
            lastIndex = max(lastIndex, last[c])

            if r == lastIndex:
                res.append(r - l + 1)
                l =  lastIndex + 1
        
        return res
        