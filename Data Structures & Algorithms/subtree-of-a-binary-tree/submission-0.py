# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r, t):
            if not r and not t:
                return True
            if not r or not t or r.val != t.val:
                return False
            
            return isSameTree(r.left, t.left) and isSameTree(r.right, t.right)
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left,subRoot)
        