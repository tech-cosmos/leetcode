class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        
        l=1
        r=1

        for i in range(n):
            ans[i]*=l
            l*=nums[i]
        
        for i in range(n-1,-1,-1):
            ans[i]*=r
            r*=nums[i]

        return ans

        