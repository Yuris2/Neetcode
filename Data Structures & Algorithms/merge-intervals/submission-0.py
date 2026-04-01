class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort the intervals with the key being lam
        intervals.sort(key=lambda i: i[0])

        mergedInterval = [intervals[0]]
        
        #Looping through [start,end] in intervals but starting at second val
        for start, end in intervals[1:]:
            #If there is an overlap
            if mergedInterval[-1][1] >= start:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], end)
            else:
                mergedInterval.append([start, end])
        
        return mergedInterval
        

        