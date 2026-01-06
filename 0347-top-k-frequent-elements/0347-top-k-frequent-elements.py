class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map={}
        res=[]
        for num in nums:
            if num in num_map:
                num_map[num]+=1
            else:
                num_map[num]=1
        
        val=sorted(list(num_map.values()), reverse=True)
        req=val[:k]
        for key in num_map:
            value=num_map[key]
            if value in req:
                res.append(key)
        return res
        