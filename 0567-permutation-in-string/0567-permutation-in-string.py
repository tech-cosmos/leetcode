from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        need=[0]*26
        win=[0]*26

        if m>n:
            return False

        for c in s1:
            need[ord(c)-97]+=1
        
        for i in range(m):
            win[ord(s2[i])-97]+=1
        
        if need==win:
            return True
        
        for i in range(m,n):
            win[ord(s2[i])-97]+=1
            win[ord(s2[i-m])-97]-=1
            if need==win:
                return True
        return False