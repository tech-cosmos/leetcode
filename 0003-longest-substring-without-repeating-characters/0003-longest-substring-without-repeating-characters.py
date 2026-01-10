from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left,ans=0,0
        for right,c in enumerate(s):
            if c in seen and seen[c]>=left:
                left=seen[c]+1
            seen[c]=right
            ans=max(ans, right-left+1)
        
        return ans
