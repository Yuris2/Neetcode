class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        index = {}

        for i, c in enumerate(s):
            index[c] = i
        
        lastIndex = 0
        prevEnd = 0

        for i, c in enumerate(s):
            lastIndex = max(lastIndex, index[c])

            if i == lastIndex:
                res.append(lastIndex - prevEnd + 1)
                prevEnd = lastIndex + 1
        
        return res
        