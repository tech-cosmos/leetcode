class Solution:
    def maxArea(self, height: List[int]) -> int:
        most=0
        l,r=0,len(height)-1
        while r>l:
            most=max(most,min(height[l], height[r])*(r-l))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return most
        