# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Approach
        #1.     Run DFS on both trees
        #2.     If both values are null, return True
        #3.     If only one value is null or values aren't equal return False

        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return dfs(p.right, q.right) and dfs(p.left, q.left)
        
        return dfs(p, q)
        