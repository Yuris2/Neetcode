class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        
        intervals.sort(key=lambda x:x[0])

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        
        return res
            
        