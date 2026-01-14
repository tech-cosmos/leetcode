class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals,prev_end=0,intervals[0][1]
        for s,e in intervals[1:]:
            if s<prev_end:
                removals+=1
            else:
                prev_end=e
        return removals