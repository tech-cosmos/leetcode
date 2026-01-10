class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        chars=[0]*26
        left,right,maxFreq,count=0,0,0,0
        for right,ch in enumerate(s):
            idx=ord(ch)-ord('A')
            chars[idx]+=1
            maxFreq=max(maxFreq, chars[idx])
            if (right-left+1)-maxFreq>k:
                chars[ord(s[left])-ord('A')]-=1
                left+=1
            count=max(count,right-left+1)
        return count
