class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[0]*(n+1)

        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        
        def union(a,b):
            ra,rb = find(a), find(b)
            if ra==rb:
                return False
            if rank[ra]>rank[rb]:
                parent[rb]=ra
            elif rank[rb]>rank[ra]:
                parent[ra]=rb
            else:
                parent[rb]=ra
                rank[ra]+=1
            return True
        
        ans=[]
        for a,b in edges:
            if not union(a,b):
                ans=[a,b]
        
        return ans
