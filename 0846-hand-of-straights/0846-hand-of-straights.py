from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        
        freq = Counter(hand)
        for x in sorted(freq):
            count=freq[x]
            if count>0:
                for v in range(x, x+groupSize):
                    if freq[v]<count:
                        return False
                    freq[v]-=count
        return True
        