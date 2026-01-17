class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(candidates)
        def dfs(start, remain):
            if remain==0:
                res.append(subset.copy())
                return
            elif remain<0:
                return
            for i in range(start, n):
                val=candidates[i]
                subset.append(val)
                dfs(i, remain-val)
                subset.pop()
        dfs(0, target)
        return res