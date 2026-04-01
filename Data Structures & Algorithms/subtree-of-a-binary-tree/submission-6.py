# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
    
    def isSameTree(self, p,q):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        