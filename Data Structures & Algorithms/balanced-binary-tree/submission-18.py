# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursiveHelper(root):
            if not root:
                return [0, True]
            
            l_info = recursiveHelper(root.left)
            r_info = recursiveHelper(root.right)
            balanced = (l_info[1] and r_info[1] and abs(l_info[0] - r_info[0]) <= 1)
            return [1 + max(r_info[0], l_info[0]), balanced]
        return recursiveHelper(root)[1]