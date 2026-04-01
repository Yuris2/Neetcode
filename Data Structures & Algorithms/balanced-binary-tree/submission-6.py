# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            depth = 0
            if root:
                left = dfs(root.left)
                right = dfs(root.right)

                if abs(left - right) > 1 or left == - 1 or right == -1:
                    return -1

                depth = 1 + max(left, right)

            
            return depth
        
        return dfs(root) != -1
        