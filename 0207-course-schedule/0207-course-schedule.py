from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for a,b in prerequisites:
            indegree[a]+=1
            graph[b].append(a)

        q=[i for i in range(numCourses) if indegree[i]==0]
        q=deque(q)
        taken=0

        while q:
            course=q.popleft()
            taken+=1
            for v in graph[course]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        
        return taken==numCourses
