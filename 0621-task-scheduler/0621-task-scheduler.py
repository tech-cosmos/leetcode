from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxheap=[-c for c in freq.values()]
        heapq.heapify(maxheap)
        cooldown=deque()
        time=0

        while maxheap or cooldown:
            time+=1


            if maxheap:
                c=1+heapq.heappop(maxheap)
                if c!=0:
                    cooldown.append((time+n, c))
            if cooldown and cooldown[0][0]==time:
                _,c=cooldown.popleft()
                heapq.heappush(maxheap,c)
        
        return time
