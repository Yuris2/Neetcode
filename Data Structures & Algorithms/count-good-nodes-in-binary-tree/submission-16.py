# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, valMax):
            nonlocal res
            if not root:
                return
            
            if root.val >= valMax:
                res += 1
            
            newMax = max(valMax, root.val)
            dfs(root.left, newMax)
            dfs(root.right, newMax)
        
        dfs(root, root.val)
        return res