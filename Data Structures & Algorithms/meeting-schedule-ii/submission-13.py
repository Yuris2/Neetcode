"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import collections
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        scheduler = []

        for i in intervals:
            start, end = i.start, i.end

            if scheduler and scheduler[0] <= start:
                heapq.heappop(scheduler)
            
            heapq.heappush(scheduler, end)
        
        return len(scheduler)

        