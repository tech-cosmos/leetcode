class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num_map=defaultdict(int)
        for num in nums:
            num_map[num]+=1
        freq=dict(sorted(num_map.items(), key=lambda x: x[1], reverse=True))
        return list(freq.keys())[:k]
        