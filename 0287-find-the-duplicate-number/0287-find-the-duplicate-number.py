from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=defaultdict(int)
        for num in nums:
            if num in seen:
                return num
            else:
                seen[num]+=1
        return 0