class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}

        for i,c in enumerate(s):
            index[c] = i
        
        res = []
        lastIndex = 0
        l = 0

        for i,c in enumerate(s):
            lastIndex = max(index[c], lastIndex)

            if lastIndex == i:
                res.append(lastIndex - l + 1)
                l = lastIndex + 1
        
        return res
        