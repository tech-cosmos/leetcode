class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        n=len(numbers)
        if n==0:
            return null
        for i in range(n):
            compliment=target-numbers[i]
            if compliment>numbers[-1]:
                continue
            r=n-1
            while numbers[r]>compliment:
                r-=1
            if numbers[r]==compliment:
                ans.append(i+1)
                ans.append(r+1)
                return ans
        