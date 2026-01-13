import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]*point[0]+point[1]*point[1]
        heap=[(distance(p),p) for p in points]
        heapq.heapify(heap)
        print("Heap : ",heap)
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans