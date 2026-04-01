# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            height = 0
            if root:
                leftHeight = dfs(root.left)
                rightHeight = dfs(root.right)

                if abs(leftHeight - rightHeight) > 1 or leftHeight == -1 or rightHeight == -1:
                    height = -1
                else:
                    height = 1 + max(leftHeight,rightHeight)

            return height
        
        return dfs(root) != -1
        