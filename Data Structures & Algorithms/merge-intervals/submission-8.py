class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])

        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
        
        return res
        