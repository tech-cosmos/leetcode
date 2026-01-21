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
        
        def dfs(node):
            if node.val in nodes:
                return nodes[node.val]
            nodes[node.val]=Node(node.val)
            for n in node.neighbors:
                nodes[node.val].neighbors.append(dfs(n))
            return nodes[node.val]
        
        return dfs(mainnode)