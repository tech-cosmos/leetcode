class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        n=len(numbers)
        for i in range(n):
            num=numbers[i]
            compliment=target-num
            if compliment>numbers[-1]:
                continue
            l=i+1
            while l<n and compliment>=numbers[l]:
                if numbers[l]==compliment:
                    ans.append(i+1)
                    ans.append(l+1)
                    return ans
                else:
                    l+=1
        