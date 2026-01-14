class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        best=float("-inf")

        while i<n:
            if i>0 and nums[i-1]>0:
                i+=1
                continue
            if nums[i]<1:
                best=max(best, nums[i])
                i+=1
                continue
            j=i+1
            local=nums[i]
            best=max(best, local)
            while j<n and local>0:
                local+=nums[j]
                best=max(best, local)
                j+=1
            i+=1
        return best

        