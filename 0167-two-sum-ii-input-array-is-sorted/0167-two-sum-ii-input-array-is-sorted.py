class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            x=target-numbers[i]
            y=numbers[:i]+numbers[i+1:]
            if x in y:
                return [i+1, y.index(x)+2]
        