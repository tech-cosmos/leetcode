class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        most=0
        l,r=0,n-1
        while r>l:
            h=min(height[l], height[r])
            vol=h*(r-l)
            if most<vol:
                most=vol
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return most
        