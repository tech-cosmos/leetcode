class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        subset=[]

        def dfs(i):
            res.append(subset.copy())
            for j in range(i, n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                subset.append(nums[j])
                dfs(j+1)
                subset.pop()
        dfs(0)
        return res
        