# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        l_info = self.lowestCommonAncestor(root.left, p, q)
        r_info = self.lowestCommonAncestor(root.right, p, q)

        if l_info and r_info:
            return root
        elif l_info:
            return l_info
        else:
            return r_info