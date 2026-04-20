# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            
            lH = dfs(node.left)
            rH = dfs(node.right)

            if abs(lH - rH) > 1 or lH == -1 or rH == -1:
                return -1
            
            return 1 + max(lH, rH)
        
        return dfs(root) != -1
        