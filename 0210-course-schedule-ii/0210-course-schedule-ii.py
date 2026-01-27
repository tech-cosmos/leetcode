from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        q=[i for i in range(numCourses) if indegree[i]==0]
        q=deque(q)
        taken=[]
        while q:
            course=q.popleft()
            taken.append(course)
            for v in graph[course]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        
        if len(taken)<numCourses:
            return []
        else:
            return taken