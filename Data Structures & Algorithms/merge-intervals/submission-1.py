class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #In place sorting 
        intervals.sort(key=lambda i: i[0])
        mergedInterval = [intervals[0]]

        #Intervals [start, end]
        for start, end in intervals:
            lastInterval = mergedInterval[-1][1]

            if start <= mergedInterval[-1][1]:
                mergedInterval[-1][1] = max(lastInterval, end)
            else:
                mergedInterval.append([start, end])
        

        return mergedInterval

        