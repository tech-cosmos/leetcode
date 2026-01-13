import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]*point[0]+point[1]*point[1]

        heap=[]
        for p in points:
            heapq.heappush(heap,(-distance(p), p))

            if len(heap)>k:
                heapq.heappop(heap)
            
        return [p for (_,p) in heap]
        