# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node,prev):
            if not node:
                return 0
            
            res = 0
            if node.val < prev:
                res = dfs(node.left,prev) + dfs(node.right,prev)
            else:
                res = 1 + (dfs(node.left, node.val) + dfs(node.right, node.val))
            
            return res
        
        return dfs(root, -2e9)


            

        

        