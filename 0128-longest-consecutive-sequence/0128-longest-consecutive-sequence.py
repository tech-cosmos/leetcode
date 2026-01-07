class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import math
        arr=sorted(set(nums))
        high=0
        count=0
        prev=-math.inf
        for num in arr:
            if count==0:
                count=1
                if high==0:
                    high=1
            if num==prev+1:
                count+=1
                if high<count:
                    high=count
            else:
                count=0
            prev=num
        
        return high