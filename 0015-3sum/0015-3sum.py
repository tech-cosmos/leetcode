class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    candidate=[nums[i],nums[j],nums[k]]
                    ans.append(candidate)
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                
        return ans