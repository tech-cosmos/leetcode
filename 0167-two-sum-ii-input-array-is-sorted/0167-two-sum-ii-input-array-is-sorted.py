class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            compliment,r=target-numbers[i], n-1
            if compliment>numbers[-1]:
                continue
            while numbers[r]>compliment:
                r-=1
            if numbers[r]==compliment:
                return [i+1, r+1]
        