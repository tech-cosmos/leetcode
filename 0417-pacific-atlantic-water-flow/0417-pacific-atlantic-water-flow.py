from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights), len(heights[0])
        res=[]

        def bfs(starts):
            vis=[[False]*n for _ in range(m)]
            q=deque(starts)
            for r,c in starts:
                vis[r][c]=True

            while q:
                r,c=q.popleft()
                for dr,dc in ((1,0),(-1,0), (0,1), (0,-1)):
                    nr,nc=r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and not vis[nr][nc]:
                        if heights[nr][nc]>=heights[r][c]:
                            vis[nr][nc]=True
                            q.append((nr,nc))
            
            return vis
        
        pac_starts=[(0,c) for c in range(n)]+ [(r,0) for r in range(m)]
        atl_starts=[(m-1,c) for c in range(n)]+ [(r,n-1) for r in range(m)]

        pac=bfs(pac_starts)
        atl=bfs(atl_starts)

        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])

       
        return res
                        