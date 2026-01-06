class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i, num in enumerate(nums):
            left=target-num
            if left in num_map:
                return [num_map[left], i]
            num_map[num]=i
