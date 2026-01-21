"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, mainnode: Optional['Node']) -> Optional['Node']:
        
        if not mainnode:
            return
        
        nodes={}
        neighbors=defaultdict(list)
        

        def cloneNode(node):
            nodes[node.val]=Node(node.val)
            for neighbor in node.neighbors:
                neighbors[node.val].append(neighbor.val)
                if neighbor.val not in nodes:
                    cloneNode(neighbor)
        
        cloneNode(mainnode)

        for val in nodes:
            nodes[val].neighbors=[nodes[n] for n in neighbors[val]]
        
        return nodes[mainnode.val]