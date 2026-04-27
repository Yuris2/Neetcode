class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        index = {}

        for i,c in enumerate(s):
            index[c] = i
        
        maxIndex = 0
        prev = 0

        for i,c in enumerate(s):
            maxIndex = max(maxIndex, index[c])

            if maxIndex == i:
                res.append(i - prev + 1)
                prev = i + 1
                maxIndex = i + 1
        
        return res
        

        