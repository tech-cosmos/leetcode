# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=True
        def height(tree):
            nonlocal balanced
            if not balanced:
                return 0
            if not tree:
                return -1
            
            l,r=height(tree.left), height(tree.right)
            if abs(l-r)>1:
                balanced=False
            
            return max(l,r)+1
        height(root)
        return balanced