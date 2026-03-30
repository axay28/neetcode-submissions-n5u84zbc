class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        theend=intervals[0][1]
        for s,e in intervals[1:]:
            if s>=theend:
                theend=e
            else:
                res+=1
                theend=min(theend,e)
        return res
       