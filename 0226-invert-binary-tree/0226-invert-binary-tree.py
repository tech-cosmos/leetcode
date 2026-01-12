# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(tree):
            if not tree:
                return
            
            temp=tree.right
            tree.right=tree.left
            tree.left=temp

            if tree.left:
                invertNode(tree.left)
            if tree.right:
                invertNode(tree.right)
        
        invertNode(root)
        return root

        