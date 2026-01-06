class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            a = nums[i]
            left=target-a
            for j in range(len(nums)):
                if nums[j]==left and j!=i:
                    ans.append(i)
                    ans.append(j)
                    break
            if len(ans)>0:
                break
        return ans        