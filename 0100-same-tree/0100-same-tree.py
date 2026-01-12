# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(first, second):
            if not first and not second:
                return 0
            if not first or not second:
                return -1
            if first.val != second.val:
                return -1

            if check(first.left, second.left) == -1:
                return -1
            if check(first.right, second.right) == -1:
                return -1

            return 0

        return check(p, q) != -1
                