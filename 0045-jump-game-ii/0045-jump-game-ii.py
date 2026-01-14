class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps=0
        end=0
        most=0

        for i,num in enumerate(nums[:-1]):
            most=max(most, i+num)

            if i==end:
                jumps+=1
                end=most
            
        return jumps
        