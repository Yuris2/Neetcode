"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)

        if len(intervals) < 2:
            return True

        for i in range(len(intervals) - 1):
            first = intervals[i].end
            second = intervals[i + 1].start

            if first > second:
                return False
        
        return True
