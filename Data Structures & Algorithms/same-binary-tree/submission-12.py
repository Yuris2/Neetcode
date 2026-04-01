# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Both are null
        if not p and not q:
            return True
        
        #If one node has a value while the other does not
        if not p or not q or p.val != q.val:
            return False
        
        #Run on left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        