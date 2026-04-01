# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftHeight = max(0,dfs(root.left))
            rightHeight = max(0,dfs(root.right))
            #Max if I took both paths
            self.res = max(self.res, root.val + leftHeight + rightHeight)
            #Max single path
            return root.val + max(leftHeight, rightHeight)
        
        dfs(root)
        return self.res
        