# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best=0
        def height(tree):
            nonlocal best
            if not tree:
                return -1
            left=tree.left
            right=tree.right

            l,r=height(tree.left), height(tree.right)

            best=max(best, l+r+2)

            return max(l,r)+1
        
        height(root)
        return best