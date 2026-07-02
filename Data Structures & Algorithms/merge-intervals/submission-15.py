class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = []
        prevStart, prevEnd = intervals[0]

        for start, end in intervals[1:]:
            if start <= prevEnd:
                prevEnd = max(prevEnd,end)
            else:
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = start,end
        
        res.append([prevStart, prevEnd])
        return res
        