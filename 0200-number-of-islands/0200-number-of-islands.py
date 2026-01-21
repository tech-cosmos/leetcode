class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        seen=[[False]*n for _ in range(m)]

        count=0
        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0:
                return
            if grid[i][j]=="0" or seen[i][j]:
                return
            
            seen[i][j]=True

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not seen[i][j]:
                    count+=1
                    dfs(i,j)
        return count
            



        