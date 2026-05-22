# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, valMax):
            if not node:
                return
            
            if node.val >= valMax:
                self.res += 1
            
            newMax = max(node.val, valMax)

            dfs(node.left, newMax)
            dfs(node.right, newMax)
        
        dfs(root, root.val)

        return self.res