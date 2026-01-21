from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board), len(board[0])
        safe=[[False]*n for _ in range(m)]

        def bfs(starts):
            q=deque()
            for r,c in starts:
                if board[r][c]=="O":
                    safe[r][c]=True
                    q.append((r,c))
            
            while q:
                r,c=q.popleft()
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and board[nr][nc]=="O" and not safe[nr][nc]:
                        safe[nr][nc]=True
                        q.append((nr,nc))
        
        starts=[(0,c) for c in range(n)]+[(r,0) for r in range(m)]+[(m-1,c) for c in range(n)]+[(r,n-1) for r in range(m)]
        bfs(starts)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and not safe[i][j]:
                    board[i][j]="X"