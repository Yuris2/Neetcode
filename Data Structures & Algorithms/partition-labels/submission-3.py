class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        end = 0
        prevEnd = 0

        for i, c in enumerate(s):
            end = max(end, lastIndex[c])

            if end == i:
                res.append(end - prevEnd + 1)
                prevEnd = i + 1
            
        return res
        