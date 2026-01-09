class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l,r=1,max(piles)

        def canEat(speed):
            time=0
            for pile in piles:
                time+=pile//speed
                if pile%speed:
                    time+=1
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


        