class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subset=[]

        def dfs(open_used, closed_used):
            if open_used==n and closed_used==n:
                res.append("".join(subset))
            
            if open_used<n:
                subset.append('(')
                dfs(open_used+1, closed_used)
                subset.pop()
            
            if closed_used<open_used:
                subset.append(')')
                dfs(open_used, closed_used+1)
                subset.pop()
        
        dfs(0,0)
        return res

