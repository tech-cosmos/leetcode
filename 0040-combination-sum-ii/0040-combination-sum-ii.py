class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(candidates)
        candidates.sort()

        def dfs(start, remain):
            if remain==0:
                res.append(subset.copy())
                return
            if remain<0:
                return
            for i in range(start,n):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                
                val=candidates[i]
                if val>remain:
                    break
                
                subset.append(val)
                dfs(i+1, remain-val)
                subset.pop()
        dfs(0, target)
        return res