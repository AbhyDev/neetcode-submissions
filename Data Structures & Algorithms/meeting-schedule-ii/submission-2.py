"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush as push, heappop as pop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda X: (X.start,X.end))
        H=[]
        for i in intervals:
            if not H:
                push(H,[i.end,i.start])
            else:
                X,Y=pop(H)
                if i.start>=X:
                    push(H,[i.end,i.start])
                else:
                    push(H,[X,Y])
                    push(H,[i.end,i.start])
        return len(H)