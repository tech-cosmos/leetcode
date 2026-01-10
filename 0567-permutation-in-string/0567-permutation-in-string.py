from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        left=0
        for right in range(window-1, len(s2)):
            if Counter(s1)==Counter(s2[left:right+1]):
                return True
            else:
                left+=1
        return False