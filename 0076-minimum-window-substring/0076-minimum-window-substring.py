from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        have=defaultdict(int)
        required=len(need)
        formed=0
        best_len=float("inf")
        best_start=0
        left=0

        for right,ch in enumerate(s):
            have[ch]+=1

            if ch in need and need[ch]==have[ch]:
                formed+=1
            
            while formed==required:
                window=right-left+1
                if window<best_len:
                    best_len=window
                    best_start=left
                left_char=s[left]
                have[left_char]-=1
                if left_char in need and have[left_char]<need[left_char]:
                    formed-=1
                left+=1
        
        return "" if best_len==float("inf") else s[best_start:best_start+best_len]