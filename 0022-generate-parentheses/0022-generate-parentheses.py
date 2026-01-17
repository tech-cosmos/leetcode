class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        a,b='(',')'

        def dfs(s="",open_used=0, closed_used=0):
            if open_used==n and closed_used==n:
                res.append(s)
            
            if open_used<n:
                dfs(s+a, open_used+1, closed_used)
            
            if closed_used<open_used:
                dfs(s+b,open_used, closed_used+1)
        
        dfs()
        return res

