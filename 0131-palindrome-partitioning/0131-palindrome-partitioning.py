class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        subset=[]
        n=len(s)

        def is_pal(l,r):
            nonlocal s
            while r>l:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True


        def dfs(start):
            if start>=n:
                res.append(subset.copy())
                return
            for end in range(start,n):
                if is_pal(start,end):
                    subset.append(s[start:end+1])
                    dfs(end+1)
                    subset.pop()
        
        dfs(0)
        return res
