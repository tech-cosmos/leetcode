class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map={}
        res=[]
        for num in nums:
            if num in num_map:
                num_map[num]+=1
            else:
                num_map[num]=1
        
        freq=dict(sorted(num_map.items(), key=lambda x: x[1], reverse=True))
        return list(freq.keys())[:k]
        