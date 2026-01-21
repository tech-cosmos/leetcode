from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        count=0
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))

        while q:
            r,c, time=q.popleft()

            for dr,dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr,nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] not in (0,2):
                    grid[nr][nc]=2
                    count=max(count, time+1)
                    q.append((nr,nc,time+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        
        return count
