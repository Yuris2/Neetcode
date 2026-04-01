"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        scheduler = []

        for interval in intervals:
            start, end = interval.start, interval.end

            #If we have rooms booked and our meeting ends before next one
            if scheduler and start >= scheduler[0]:
                heapq.heappop(scheduler)
            
            #Book a room
            heapq.heappush(scheduler, end)
            
        
        return len(scheduler)

        