# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=defaultdict(int)
        q=deque([(root,0)])
        while q:
            node,i=q.popleft()
            if not node:
                continue
            ans[i]=node.val
            if node.left:
                q.append((node.left,i+1))
                ans[i]=node.val
            if node.right:
                q.append((node.right,i+1))
                ans[i]=node.val
        
        return list(ans.values())