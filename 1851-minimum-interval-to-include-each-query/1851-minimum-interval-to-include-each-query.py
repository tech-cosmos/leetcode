import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries_sorted=sorted([(q,i) for i,q in enumerate(queries)])
        res=[-1]*len(queries)
        i=0
        n=len(intervals)
        heap=[]

        for q,qi in queries_sorted:
            while i<n and intervals[i][0]<=q:
                s,e=intervals[i]
                heapq.heappush(heap, (e-s+1, e))
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            
            if heap:
                res[qi]=heap[0][0]
        
        return res

        