# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            depth = 0
            if root:
                lH = dfs(root.left)
                rH = dfs(root.right)

                self.diameter = max(self.diameter, lH + rH)

                depth = 1 + max(lH, rH)
            
            return depth
        
        dfs(root)

        return self.diameter


        