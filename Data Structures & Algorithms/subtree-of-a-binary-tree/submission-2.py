# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t,s):
            if not t and not s:
                return True
            
            if not t or not s or s.val != t.val:
                return False
            
            return isSameTree(t.right, s.right) and isSameTree(t.left, s.left)
        
        #if subroot is null, always subtree
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        