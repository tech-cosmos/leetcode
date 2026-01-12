# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack=deque([(root,0)])
        ans=[]
        while stack:
            node,i=stack.popleft()
            if not node:
                continue
            if len(ans)<=i:
                ans.append([node.val])
            else:
                ans[i].append(node.val)
            if node.left:
                stack.append((node.left,i+1))
            if node.right:
                stack.append((node.right,i+1))
        return ans




        