class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        has_x, has_y, has_z=False,False,False

        for (a,b,c) in triplets:
            if a>x or b>y or c>z:
                continue
            if x==a:
                has_x=True
            if y==b:
                has_y=True
            if z==c:
                has_z=True
            
            if has_x and has_y and has_z:
                return True
        
        return False
        