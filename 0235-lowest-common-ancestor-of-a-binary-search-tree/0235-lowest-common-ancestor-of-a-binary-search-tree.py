# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval,qval=p.val,q.val
        while True:
            if pval>root.val and qval>root.val:
                root=root.right
            elif pval<root.val and qval<root.val:
                root=root.left
            else:
                return root
            