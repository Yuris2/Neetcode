# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, node: Optional[TreeNode]) -> int:
        self.res = -2e9

        def dfs(root):
            if not root:
                return 0
            
            lH = max(0,dfs(root.left))
            rH = max(0,dfs(root.right))


            self.res = max(self.res, root.val + lH + rH)

            return root.val + max(lH, rH)
        
        dfs(node)
        return self.res
        