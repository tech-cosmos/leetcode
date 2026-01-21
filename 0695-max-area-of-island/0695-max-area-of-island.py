class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        seen=[[False]*n for _ in range(m)]

        maxArea,count=0,0
        def dfs(i,j):
            nonlocal count
            if i>=m or i<0 or j>=n or j<0 or seen[i][j] or grid[i][j]==0:
                return
            
            seen[i][j]=True
            count+=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    maxArea=max(maxArea, count)
                    count=0
        
        return maxArea
        