class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        res=[]
        for s,e in intervals:
            if not res or s>=res[-1][1]:
                res.append([s,e])
            else:
                res[-1][1]=min(res[-1][1], e)
        return len(intervals)-len(res)