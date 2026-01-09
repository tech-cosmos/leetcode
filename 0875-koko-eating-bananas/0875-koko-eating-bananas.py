from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=ceil(sum(piles)/h),max(piles)

        def canEat(speed):
            time=0
            for pile in piles:
                time+=ceil(pile/speed)
                if time>h:
                    return False
            return True
        
        while l<r:
            mid=(l+r)//2
            if canEat(mid):
                r = mid
            else:
                l=mid+1
        return l


        